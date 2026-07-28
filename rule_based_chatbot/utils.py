# =============================================================
# utils.py
# PURPOSE : All visual/display utilities in one place.
#           Professionals never scatter print statements with
#           color codes throughout the codebase. Centralize it.
# =============================================================

import os
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama — required on Windows for ANSI codes to work
init(autoreset=True)   # autoreset=True means color resets after every print automatically


# ── COLOR CONSTANTS ───────────────────────────────────────────
# Define your color scheme here — change only here if redesigning
BOT_COLOR    = Fore.CYAN       # Bot responses
USER_COLOR   = Fore.GREEN      # User input prompt
ERROR_COLOR  = Fore.RED        # Errors / unknowns
INFO_COLOR   = Fore.YELLOW     # System messages / stats
ACCENT_COLOR = Fore.MAGENTA    # Headers and decorators
DIM_COLOR    = Style.DIM       # Secondary/dim text
RESET        = Style.RESET_ALL # Full reset


# ── DISPLAY FUNCTIONS ─────────────────────────────────────────

def print_banner():
    """Prints the startup banner when the chatbot launches."""
    banner = f"""
{ACCENT_COLOR}{'='*65}
   ___    ____  ____  ___
  / _ |  / __ \\/  _/ / _ |
 / __ | / /_/ // /  / __ |
/_/ |_|/_/ |_/___/ /_/ |_|

  Automated Rule-based Intelligence Assistant  v1.0
  DecodeLabs AI Internship — Project 1
  Architecture : IPO Model  |  Lookup : O(1) Hash Map
  Python 3.14  |  Type 'help' for commands
{'='*65}{RESET}
"""
    print(banner)


def print_bot(message: str):
    """Prints a formatted bot response."""
    print(f"\n{BOT_COLOR}  🤖 ARIA ▸{RESET}  {message}\n")


def print_system(message: str):
    """Prints a system/info message (not a bot response)."""
    print(f"{INFO_COLOR}  ⚙  {message}{RESET}")


def print_error(message: str):
    """Prints an error or fallback message."""
    print(f"\n{ERROR_COLOR}  ⚠  ARIA ▸{RESET}  {message}\n")


def print_separator():
    """Prints a visual separator line."""
    print(f"{DIM_COLOR}  {'─'*60}{RESET}")


def print_exit_message(stats: dict):
    """Prints the session summary when user exits."""
    duration = datetime.now() - stats["start_time"]
    minutes  = int(duration.total_seconds() // 60)
    seconds  = int(duration.total_seconds() % 60)

    print(f"""
{ACCENT_COLOR}{'='*65}
  SESSION SUMMARY
{'='*65}{RESET}
{INFO_COLOR}  Total Messages Sent   :  {stats['total_messages']}
  Matched (Exact)       :  {stats['exact_matches']}
  Matched (Keyword)     :  {stats['keyword_matches']}
  Unmatched (Fallback)  :  {stats['fallbacks']}
  Session Duration      :  {minutes}m {seconds}s
{ACCENT_COLOR}{'='*65}
  Goodbye! Keep building. 🚀
{'='*65}{RESET}
""")


def get_user_prompt() -> str:
    """Returns the styled user input prompt string."""
    return f"{USER_COLOR}  You ▸{RESET}  "


def clear_screen():
    """Clears the terminal screen cross-platform."""
    os.system('cls' if os.name == 'nt' else 'clear')


def format_datetime_response(mode: str) -> str:
    """Returns current time or date as a formatted bot response."""
    now = datetime.now()
    if mode == "time":
        return f"The current time is: {now.strftime('%I:%M:%S %p')}"
    elif mode == "date":
        return f"Today's date is: {now.strftime('%A, %B %d, %Y')}"
    return ""