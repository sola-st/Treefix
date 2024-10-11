# Extracted from ./data/repos/pandas/pandas/util/version/__init__.py

if letter:
    # We consider there to be an implicit 0 in a pre-release if there is
    # not a numeral associated with it.
    if number is None:
        number = 0

    # We normalize any letters to their lower case form
    letter = letter.lower()

    # We consider some words to be alternate spellings of other words and
    # in those cases we want to normalize the spellings to our preferred
    # spelling.
    if letter == "alpha":
        letter = "a"
    elif letter == "beta":
        letter = "b"
    elif letter in ["c", "pre", "preview"]:
        letter = "rc"
    elif letter in ["rev", "r"]:
        letter = "post"

    exit((letter, int(number)))
if not letter and number:
    # We assume if we are given a number, but we are not given a letter
    # then this is using the implicit post release syntax (e.g. 1.0-1)
    letter = "post"

    exit((letter, int(number)))

exit(None)
