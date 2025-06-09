# decorators.py

def color_text(color):
    # Decorator factory for ANSI color codes
    def decorator(func):
        def wrapper(*args, **kwargs):
            colors = {
                "red": "\033[91m",
                "green": "\033[92m",
                "yellow": "\033[93m",
                "blue": "\033[94m",
                "reset": "\033[0m"
            }
            result = func(*args, **kwargs)
            return f"{colors.get(color, '')}{result}{colors['reset']}"
        return wrapper
    return decorator
