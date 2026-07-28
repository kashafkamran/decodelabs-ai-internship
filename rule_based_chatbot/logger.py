# =============================================================
# logger.py
# PURPOSE : Handles all file I/O for chat history.
#           Real-world chatbots always log conversations for
#           audit trails, debugging, and quality review.
#           This is your compliance & traceability module.
# =============================================================

import os
from datetime import datetime


# ── CONSTANTS ─────────────────────────────────────────────────
LOG_DIR = "chat_logs"   # All logs saved in this subfolder


def initialize_log() -> str:
    """
    Creates the chat_logs/ directory if it doesn't exist,
    then creates a new timestamped log file for this session.
    Returns the log file path so chatbot.py can pass it around.
    """
    # Create directory if it doesn't exist
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # Generate a unique filename using timestamp
    timestamp   = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"{LOG_DIR}/session_{timestamp}.txt"

    # Write the session header into the log file
    with open(log_filename, "w", encoding="utf-8") as log_file:
        log_file.write("=" * 60 + "\n")
        log_file.write("  ARIA — Rule-Based AI Chatbot | Chat Log\n")
        log_file.write(f"  Session Started : {datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}\n")
        log_file.write("=" * 60 + "\n\n")

    return log_filename


def log_exchange(log_path: str, user_input: str, bot_response: str, match_type: str):
    """
    Appends a single conversation exchange to the log file.

    Args:
        log_path     : Path to the active log file
        user_input   : Raw user message (before sanitization)
        bot_response : The bot's reply
        match_type   : 'EXACT', 'KEYWORD', 'FALLBACK', or 'SYSTEM'
    """
    timestamp = datetime.now().strftime("%H:%M:%S")

    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] [{match_type}]\n")
        log_file.write(f"  USER : {user_input}\n")
        log_file.write(f"  ARIA : {bot_response}\n")
        log_file.write("\n")


def finalize_log(log_path: str, stats: dict):
    """
    Writes the session summary at the bottom of the log file
    when the user exits. Mirrors what's shown on screen.
    """
    duration = datetime.now() - stats["start_time"]
    minutes  = int(duration.total_seconds() // 60)
    seconds  = int(duration.total_seconds() % 60)

    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write("\n" + "=" * 60 + "\n")
        log_file.write("  SESSION SUMMARY\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"  Total Messages    : {stats['total_messages']}\n")
        log_file.write(f"  Exact Matches     : {stats['exact_matches']}\n")
        log_file.write(f"  Keyword Matches   : {stats['keyword_matches']}\n")
        log_file.write(f"  Fallbacks         : {stats['fallbacks']}\n")
        log_file.write(f"  Session Duration  : {minutes}m {seconds}s\n")
        log_file.write(f"  Session Ended     : {datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}\n")
        log_file.write("=" * 60 + "\n")