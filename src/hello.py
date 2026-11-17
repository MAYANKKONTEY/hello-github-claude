"""A small hello program, built with Claude Code."""


def greet(name: str = "GitHub") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! 👋"


def main() -> None:
    print(greet())
    print("I build this project using Claude Code.")

    # Count from 1 to 5
    for number in range(1, 6):
        print(f"Count: {number}")


if __name__ == "__main__":
    main()
