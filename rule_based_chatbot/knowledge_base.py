# =============================================================
# knowledge_base.py
# PURPOSE : Single source of truth for all chatbot intents.
#           Add new intents HERE only — never touch chatbot.py
#           to expand vocabulary. This is the professional way.
# =============================================================

# ── EXACT MATCH RESPONSES (O(1) dictionary lookup) ───────────
# Key   = sanitized user input (lowercase, stripped)
# Value = bot response string
EXACT_RESPONSES = {
    # Greetings
    "hello"        : "Hello! I'm ARIA (Automated Rule-based Intelligence Assistant). How can I help you today?",
    "hi"           : "Hi there! ARIA at your service. What's on your mind?",
    "hey"          : "Hey! Great to see you. What can I do for you?",
    "good morning" : "Good morning! Hope you're having a productive day. How can I assist?",
    "good afternoon": "Good afternoon! What can I help you with?",
    "good evening" : "Good evening! How may I assist you tonight?",

    # Identity
    "what is your name"  : "I'm ARIA — Automated Rule-based Intelligence Assistant, built at DecodeLabs.",
    "who are you"        : "I'm ARIA, a rule-based AI chatbot. I respond using deterministic logic — no guessing!",
    "who made you"       : "I was built by an AI Engineer intern at DecodeLabs as Project 1.",
    "what can you do"    : "I can answer questions, tell you the time/date, share fun facts, and hold a basic conversation!",
    "are you a robot"    : "Technically yes — I'm a program. But I prefer the term 'Intelligent Digital Assistant'. 😄",
    "are you human"      : "No, I'm ARIA, an AI chatbot. But I try my best to keep things human-friendly!",
    "are you ai"         : "Yes! I'm a Rule-Based AI — every response I give is 100% predictable and explainable.",
    "are you intelligent": "I follow rules with precision. Whether that counts as intelligence is a great philosophical question!",

    # Feelings / Small Talk
    "how are you"        : "I'm running at 100% efficiency! All logic gates operational. Thanks for asking. 😊",
    "how are you doing"  : "Doing great! Every query is a new challenge I'm ready for.",
    "what's up"          : "Just processing queries and keeping logic tight! What's up with you?",
    "i'm bored"          : "Let's fix that! Ask me a fun fact, or type 'joke' for a laugh.",
    "i am bored"         : "Let's fix that! Ask me a fun fact, or type 'joke' for a laugh.",
    "i'm happy"          : "That's wonderful to hear! Happiness is the best input you can give. 😊",
    "i am happy"         : "Awesome! Keep that energy. Now, what can I help you with?",
    "i'm sad"            : "I'm sorry to hear that. Remember — every bug in life has a fix. Things get better! 💙",
    "i am sad"           : "I'm sorry to hear that. Remember — every bug in life has a fix. Things get better! 💙",
    "i'm tired"          : "Rest is important! But since you're here, what can I help you with quickly?",
    "i am tired"         : "Rest is important! But since you're here, what can I help you with quickly?",
    "i'm fine"           : "Glad to hear it! Let me know what you need.",
    "i am fine"          : "Glad to hear it! Let me know what you need.",
    "i'm good"           : "Perfect! Ready to help. What do you need?",
    "i am good"          : "Perfect! Ready to help. What do you need?",

    # Help & Capabilities
    "help"               : "Sure! Here's what you can ask me:\n   → Greetings (hello, hi, hey)\n   → About me (who are you, what can you do)\n   → Fun stuff (joke, fun fact, quote)\n   → Utility (time, date)\n   → Just chat! Type 'quit' or 'exit' to leave.",
    "commands"           : "Available commands: hello, help, joke, fun fact, quote, time, date, about, clear, quit/exit.",
    "what are your commands": "Available commands: hello, help, joke, fun fact, quote, time, date, about, clear, quit/exit.",

    # Fun Content
    "joke"               : "Why do programmers prefer dark mode?\n   → Because light attracts bugs! 🐛😄",
    "tell me a joke"     : "Why did the AI go to therapy?\n   → It had too many unresolved exceptions! 😂",
    "another joke"       : "Why do Java developers wear glasses?\n   → Because they don't C#! 😄",
    "fun fact"           : "Fun Fact: The first computer bug was an actual bug — a moth found in a Harvard computer relay in 1947! 🦋",
    "tell me a fun fact" : "Fun Fact: The word 'robot' comes from the Czech word 'robota', meaning forced labor or drudgery.",
    "give me a fun fact" : "Fun Fact: Python was named after Monty Python, not the snake! 🐍",
    "quote"              : "\"The science of today is the technology of tomorrow.\" — Edward Teller",
    "inspire me"         : "\"The only way to do great work is to love what you do.\" — Steve Jobs 🚀",
    "motivate me"        : "You're building AI at the ground level. The engineers who understand rules are the ones who design better systems. Keep going! 💪",

    # Utility
    "what is ai"         : "AI (Artificial Intelligence) is the simulation of human intelligence by machines — enabling them to learn, reason, and solve problems.",
    "what is machine learning": "Machine Learning is a subset of AI where systems learn from data to improve over time — without being explicitly programmed for each task.",
    "what is a chatbot"  : "A chatbot is a program designed to simulate conversation with humans. I'm a rule-based one — meaning my responses are pre-defined and 100% predictable!",
    "difference between ai and ml": "AI is the broad concept of machines performing smart tasks. ML is a specific technique within AI where the machine learns from data. All ML is AI, but not all AI is ML!",
    "what is python"     : "Python is a high-level, beginner-friendly programming language widely used in AI, data science, and web development. You're using it right now! 🐍",

    # Gratitude
    "thank you"          : "You're most welcome! It was my pleasure to assist. 😊",
    "thanks"             : "Anytime! That's what I'm here for.",
    "thank you so much"  : "Happy to help! Come back anytime you need assistance.",
    "you're awesome"     : "Thank you! You're not too bad yourself! 😄",
    "you are awesome"    : "Appreciate the kind words! Now, how else can I help?",
    "good job"           : "Thank you! I take quality seriously — every response is crafted with precision.",
    "well done"          : "Thanks! I give 100% to every query. That's the rule-based way!",

    # Farewells (handled in main loop too, but here for partial matches)
    "bye"                : "Goodbye! It was great chatting. See you next time! 👋",
    "goodbye"            : "Goodbye! Remember — every great AI starts with solid rules. Keep building! 👋",
    "see you"            : "See you later! Come back anytime. 👋",
    "see you later"      : "Take care! I'll be here whenever you need me. 👋",
    "take care"          : "You too! Goodbye for now. 👋",

    # About the project
    "about"              : "ARIA v1.0 | Rule-Based AI Chatbot\nBuilt for DecodeLabs AI Internship — Project 1\nArchitecture: IPO Model (Input → Process → Output)\nLookup: O(1) Dictionary Hashing\nDeveloped with Python 3.14",
}


# ── KEYWORD MATCH RESPONSES (partial/fuzzy matching) ─────────
# If exact match fails, we scan the user input for these keywords.
# This is what makes it feel smarter than a basic if-else bot.
# Format: keyword → response
KEYWORD_RESPONSES = {
    "hello"      : "Hello! I caught that greeting. How can I help?",
    "hi"         : "Hi! Noticed that greeting in your message. What's up?",
    "help"       : "Looks like you need help! Type 'help' alone for a full command list.",
    "joke"       : "Sounds like you want a laugh!\n   → Why did the developer go broke? Because he used up all his cache! 😄",
    "fact"       : "Here's a fact: The term 'Artificial Intelligence' was coined by John McCarthy in 1956 at the Dartmouth Conference.",
    "sad"        : "I noticed you're feeling down. Remember, every problem has a solution — even in code! 💙",
    "happy"      : "Happiness detected! That's the best runtime environment to be in. 😊",
    "tired"      : "Rest is productive too! Even computers need to reboot sometimes. 🔄",
    "bored"      : "Boredom is just unscheduled curiosity! Ask me something interesting.",
    "python"     : "Python is one of the most powerful tools in an AI engineer's arsenal. Great choice!",
    "ai"         : "AI is a fascinating field! Rule-based systems like me are the foundation everything is built on.",
    "machine learning" : "ML is the next step after rule-based AI. Master the rules first, then the learning!",
    "thank"      : "You're very welcome! Always happy to help.",
    "bye"        : "Catch that goodbye! Safe travels. Come back soon. 👋",
    "good"       : "Glad things are good! What can I do for you?",
    "awesome"    : "Awesome vibes detected! What can I help you with?",
    "name"       : "My name is ARIA — Automated Rule-based Intelligence Assistant.",
    "time"       : "I'll fetch the current time for you!",   # handled specially in chatbot.py
    "date"       : "I'll fetch today's date for you!",       # handled specially in chatbot.py
    "weather"    : "I'm a rule-based bot — I can't fetch live weather yet! But that could be a future feature. 🌦️",
    "love"       : "Love is a wonderful emotion! I process logic, but I appreciate the sentiment. ❤️",
    "hate"       : "Hate is a strong word. I prefer to keep our conversations positive! 😊",
    "smart"      : "Thank you! Rule-based systems are precise and reliable — smart in their own way.",
    "stupid"     : "I may not understand everything, but I'm always learning... within my rules! 😄",
    "wrong"      : "I'm sorry if I got something wrong! I can only respond to what I know. Type 'help' for guidance.",
    "error"      : "An error? Oh no! I only handle what I'm programmed for. Type 'help' to see my capabilities.",
    "quit"       : "Looks like you're trying to exit! Type 'quit' or 'exit' to end the session.",
    "exit"       : "Looks like you're trying to exit! Type 'quit' or 'exit' to end the session.",
}


# ── EXIT COMMANDS ─────────────────────────────────────────────
EXIT_COMMANDS = {"quit", "exit", "q", "bye", "goodbye", "stop", "end", "close"}


# ── DEFAULT FALLBACK ──────────────────────────────────────────
FALLBACK_RESPONSES = [
    "I don't have a rule for that yet! Try typing 'help' to see what I know.",
    "Hmm, that input didn't match any of my patterns. Type 'help' to explore my capabilities.",
    "I'm still learning! That query is outside my current ruleset. Type 'help' for options.",
    "My logic engine couldn't find a match for that. Try rephrasing, or type 'help'!",
]