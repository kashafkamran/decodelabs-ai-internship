# =============================================================
# chatbot.py
# PURPOSE : Main entry point. Orchestrates the full IPO pipeline:
#             Phase 1 → INPUT    (sanitization)
#             Phase 2 → PROCESS  (intent matching)
#             Phase 3 → OUTPUT   (response + logging)
#
# ARCHITECTURE NOTE:
#   We use a dictionary (.get()) for O(1) lookups — NOT if-elif.
#   The if-elif ladder is O(n) and is an explicit anti-pattern
#   highlighted in the project specification.
# =============================================================

import random
from datetime import datetime

# Local module imports
from knowledge_base import (
    EXACT_RESPONSES,
    KEYWORD_RESPONSES,
    FALLBACK_RESPONSES,
    EXIT_COMMANDS,
)
from utils import (
    print_banner,
    print_bot,
    print_system,
    print_error,
    print_separator,
    print_exit_message,
    get_user_prompt,
    clear_screen,
    format_datetime_response,
)
from logger import initialize_log, log_exchange, finalize_log


# ── PHASE 1: INPUT SANITIZATION ───────────────────────────────

def sanitize(raw_input: str) -> str:
    """
    Normalizes raw user input so the logic engine can match it
    reliably regardless of how the user typed it.

    Steps:
        1. Strip leading/trailing whitespace
        2. Convert to lowercase
        3. Remove punctuation that isn't part of meaning

    Example:
        "  Hello!!  " → "hello"
        "WHAT IS AI?" → "what is ai"
    """
    cleaned = raw_input.strip().lower()

    # Remove common punctuation (keeps apostrophes for contractions)
    chars_to_remove = ['!', '?', '.', ',', ';', ':', '"', '(', ')', '[', ']']
    for char in chars_to_remove:
        cleaned = cleaned.replace(char, '')

    # Collapse multiple spaces into one
    cleaned = ' '.join(cleaned.split())

    return cleaned


# ── PHASE 2: INTENT MATCHING (PROCESS) ────────────────────────

def match_intent(clean_input: str) -> tuple[str, str]:
    """
    The core logic engine. Runs a 3-tier matching strategy:

    Tier 1 — Exact Match  : O(1) dictionary lookup (fastest)
    Tier 2 — Keyword Match: scans input for known keywords
    Tier 3 — Fallback     : random response from fallback list

    Returns:
        (response_string, match_type_string)
        match_type is 'EXACT', 'KEYWORD', or 'FALLBACK'
    """

    # ── TIER 1: EXACT MATCH (O(1) hash lookup) ────────────────
    # .get() returns the value if found, None if not.
    # This replaces the entire if-elif ladder — O(1) vs O(n).
    response = EXACT_RESPONSES.get(clean_input)
    if response:
        return response, "EXACT"

    # ── TIER 2: KEYWORD SCAN (partial/fuzzy match) ─────────────
    # Checks if any known keyword appears anywhere in the input.
    # This catches sentences like "I feel happy today" → happy intent
    for keyword, keyword_response in KEYWORD_RESPONSES.items():
        if keyword in clean_input:
            return keyword_response, "KEYWORD"

    # ── TIER 3: FALLBACK ───────────────────────────────────────
    # Nothing matched — return a random fallback so it doesn't
    # feel repetitive to the user.
    return random.choice(FALLBACK_RESPONSES), "FALLBACK"


# ── PHASE 3: SPECIAL COMMANDS ─────────────────────────────────

def handle_special_commands(clean_input: str) -> tuple[str, str] | None:
    """
    Handles commands that need live data or system actions —
    things that can't be stored in a static dictionary.

    Returns (response, match_type) if handled, else None.
    """
    if "time" in clean_input:
        return format_datetime_response("time"), "SYSTEM"

    if "date" in clean_input:
        return format_datetime_response("date"), "SYSTEM"

    if clean_input == "clear":
        clear_screen()
        print_banner()
        return "Screen cleared! Fresh start. 🧹", "SYSTEM"

    return None  # Not a special command — continue normal flow


# ── MAIN LOOP (THE HEARTBEAT) ──────────────────────────────────

def run_chatbot():
    """
    The core infinite loop — the chatbot's heartbeat.
    Stays alive until the user sends a kill command.

    Loop structure:
        while True:
            1. Get input
            2. Sanitize
            3. Check exit
            4. Check special commands
            5. Match intent
            6. Output response
            7. Log exchange
    """

    # ── STARTUP ───────────────────────────────────────────────
    clear_screen()
    print_banner()
    print_system("Session started. Type 'help' for commands, 'quit' to exit.")
    print_separator()

    # Initialize session log file
    log_path = initialize_log()
    print_system(f"Chat log started → {log_path}")
    print_separator()

    # Opening greeting from bot
    opening = "Hello! I'm ARIA — your Rule-Based AI Assistant. What can I help you with today? 😊"
    print_bot(opening)

    # ── SESSION STATISTICS (tracked in memory) ────────────────
    stats = {
        "start_time"     : datetime.now(),
        "total_messages" : 0,
        "exact_matches"  : 0,
        "keyword_matches": 0,
        "fallbacks"      : 0,
    }

    # ── THE INFINITE LOOP ─────────────────────────────────────
    while True:

        # ── PHASE 1: INPUT ────────────────────────────────────
        try:
            raw_input = input(get_user_prompt())
        except (KeyboardInterrupt, EOFError):
            # Catches Ctrl+C — exits gracefully instead of crashing
            print()   # New line for clean formatting
            print_system("Keyboard interrupt detected. Shutting down gracefully...")
            break

        # Skip empty input — don't process blank Enter presses
        if not raw_input.strip():
            print_system("(Empty input received — please type something!)")
            continue

        # Sanitize the raw input → clean, normalized string
        clean_input = sanitize(raw_input)

        # ── EXIT CHECK ────────────────────────────────────────
        # Check against a SET (O(1) lookup) — not a list
        if clean_input in EXIT_COMMANDS:
            farewell = "Goodbye! It was great chatting. Keep building great things! 🚀👋"
            print_bot(farewell)
            log_exchange(log_path, raw_input, farewell, "SYSTEM")
            break

        # Update message counter
        stats["total_messages"] += 1

        # ── PHASE 2: PROCESS ──────────────────────────────────

        # Check special commands first (time, date, clear)
        special_result = handle_special_commands(clean_input)

        if special_result:
            response, match_type = special_result
        else:
            # Run the 3-tier intent matching engine
            response, match_type = match_intent(clean_input)

        # ── UPDATE STATS ──────────────────────────────────────
        if match_type == "EXACT":
            stats["exact_matches"]   += 1
        elif match_type == "KEYWORD":
            stats["keyword_matches"] += 1
        elif match_type == "FALLBACK":
            stats["fallbacks"]       += 1

        # ── PHASE 3: OUTPUT ───────────────────────────────────
        if match_type == "FALLBACK":
            print_error(response)   # Red color for unmatched
        else:
            print_bot(response)     # Cyan color for matched

        # Show match type as a subtle hint (professional transparency)
        print_system(f"[Match: {match_type}]")
        print_separator()

        # Log this exchange to file
        log_exchange(log_path, raw_input, response, match_type)


    # ── SESSION END ───────────────────────────────────────────
    finalize_log(log_path, stats)
    print_exit_message(stats)
    print_system(f"Full chat log saved → {log_path}")


# ── ENTRY POINT ───────────────────────────────────────────────
# This block ensures run_chatbot() is only called when this file
# is executed directly — not when imported as a module.
# This is standard Python professional practice.
if __name__ == "__main__":
    run_chatbot()