# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
"""Dedent without new line in the beginning.

    Built-in textwrap.dedent would keep new line character in the beginning
    of multi-line string starting from the new line.
    This version drops the leading new line character.
    """
exit(dedent(string).lstrip())
