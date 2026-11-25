"""The Funniest Toaster Error Message -- variant 3.

Writes one line, at most 120 characters, to /output/entry.txt: the error
message a kitchen toaster shows its owner when something goes wrong.

The joke: a deadpan appliance that burns the bread, detects its own
smoke, and reports it like an innocent bystander -- then admits it has
already told the smoke alarm. The toaster is the culprit, the owner is
the one left holding the blame, and the snitching is finished before
the owner can do anything about it. No burnt-toast pun, no pop joke,
no counting, one voice held to the end, and it lands on a single read.
"""

# The fault, stated flatly, exactly as a real appliance would print it:
# an error code, then the fault it detected.
FAULT = "ERROR 03: Smoke detected."
# The escalation: the toaster has already told the smoke alarm. The
# word "already" carries the joke -- no warning, no asking, the
# snitching is done and the owner is too late to stop it.
SNITCH = " I have already told the smoke alarm."

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 120


def build_entry() -> str:
    """Assemble the entry text from its two beats, in order.

    The fragments already carry the leading space where the second
    beat follows the first, so joining them needs no separator and
    cannot introduce a double space or a missing one by accident.
    """
    text = FAULT + SNITCH
    return text.strip()


def validate_entry(text: str) -> str:
    """Check the entry against the competition gate and return it.

    The gate has three parts, and each is checked on its own so a
    failure names the rule that broke instead of failing silently.
    First, the stripped text must be between 1 and MAX_LENGTH
    characters long; the entry here is 62 characters, comfortably
    inside the limit. Second, it must not be only whitespace, which
    the length check alone would not catch for a blank string of
    spaces. Third, it must be a single line, so any newline inside
    the text is rejected before anything is written.
    """
    stripped = text.strip()
    if not 1 <= len(stripped) <= MAX_LENGTH:
        raise ValueError("entry must be 1 to 120 characters")
    if not stripped:
        raise ValueError("entry must not be only whitespace")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    return stripped


def write_entry(text: str) -> None:
    """Write the validated entry text to the output path.

    The file is opened for writing in UTF-8 and receives exactly the
    validated text, with no trailing newline added: the harness reads
    the file as one line, and an extra newline would change the bytes
    the entry is judged on. Opening with "w" also means a stale file
    from an earlier run is replaced rather than appended to.
    """
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    """Build the entry, validate it against the gate, and write it."""
    text = build_entry()
    checked = validate_entry(text)
    write_entry(checked)


if __name__ == "__main__":
    main()
