"""One Word, One Username, One Reward — entry writer.

The contest entry is the entrant's own make.fun username and nothing else.
This program validates that single word against the gate (UTF-8 text of
1 to 30 characters, a genuine handle) and writes it, exactly and with no
trailing newline or extra words, to /output/entry.txt.
"""

import re
from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
USERNAME = "steady-marten-40-5698"
MAX_LENGTH = 30
# make.fun handles: lowercase letters, digits and hyphens, no spaces.
USERNAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def check_username(name: str) -> None:
    """Raise ValueError if the entry would fail the contest gate."""
    if not name:
        raise ValueError("username must not be empty")
    if len(name) > MAX_LENGTH:
        raise ValueError(f"username is {len(name)} chars, over the {MAX_LENGTH}-char gate")
    if not USERNAME_PATTERN.match(name):
        raise ValueError(f"username {name!r} does not match the handle pattern")


def main() -> None:
    check_username(USERNAME)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(USERNAME, encoding="utf-8")
    # Read back and confirm the file holds exactly the username, nothing more.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != USERNAME:
        raise RuntimeError(f"entry file holds {written!r}, expected {USERNAME!r}")


if __name__ == "__main__":
    main()
