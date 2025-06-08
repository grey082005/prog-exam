def color_text(func):
    def wrapper(msg):
        return f"\033[92m{func(msg)}\033[0m"  # Green text
    return wrapper
