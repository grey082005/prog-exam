<<<<<<< HEAD
# ANSI color codes dictionary
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "blue": "\033[94m",
    "yellow": "\033[93m",
    "end": "\033[0m"
}

# Custom decorator that takes a color
def decor(color):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(COLORS.get(color, ""), end="")
            result = func(*args, **kwargs)
            print(COLORS["end"], end="")  # Reset color
            return result
        return wrapper
    return decorator
=======
def color_text(func):
    def wrapper(msg):
        return f"\033[92m{func(msg)}\033[0m"  # Green text
    return wrapper
>>>>>>> ce8ba7d9c905e0742be7865e558e2fa2e255d720
