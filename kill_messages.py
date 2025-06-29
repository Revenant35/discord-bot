import random

def get_kill_message(name):
    messages = [
        f"{name} has been redacted from reality.",
        f"{name} is now just a rumor in the server logs.",
        f"{name} is now legally classified as a myth.",
        f"{name} has been voted off the server by a shadowy cabal.",
        f"{name} is now a cautionary tale told to new users.",
        f"{name} is now the reason for a new server rule.",
        f"{name} discovered that it *was not* Michael.",
    ]
    return random.choice(messages)

def get_not_in_channel_message(name):
    messages = [
        f"{name} is currently quantum tunneling between channels. Try again later.",
        f"{name} is hiding in the server's crawlspace.",
    ]
    return random.choice(messages)

def get_no_user_message():
    messages = [
        "No target? No disconnect. The bot demands a name.",
        "Please tag a user. The algorithm must be appeased.",
        "The void stares back. Please @ someone to banish them.",
    ]
    return random.choice(messages)
