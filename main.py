"""Unsent: The Micro-Confession Sprint.

A two-part micro-confession: a To: line naming who it was meant for, and
the unsent message itself, one line written exactly as it was typed. The
confession is small and painfully relatable — reading every message the
instant it arrives, then waiting three days to reply to look busy.
Gate: 1-260 characters total; the message itself at most 200 characters.
"""

TO_LINE = "To: the group chat"

MESSAGE = (
    "I read every message the second it arrived. I just waited three days "
    "to reply so you'd think I have a life."
)


def check_confession(to_line: str, message: str) -> str:
    """A confession needs its addressee and a message that was never sent."""
    assert to_line.startswith("To: "), "first part must be a To: line"
    assert "read every message" in message, "confession lost its guilty core"
    assert "three days" in message, "confession lost its delay"
    return to_line + "\n" + message


def main() -> None:
    message = " ".join(MESSAGE.split())
    assert 1 <= len(message) <= 200, f"message is {len(message)} chars, max 200"
    assert "\n" not in message, "message must be a single line"
    text = check_confession(TO_LINE, message)
    assert 1 <= len(text) <= 260, f"entry is {len(text)} chars, gate is 1-260"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
