# Extracted from ./data/repos/pandas/pandas/core/computation/parsing.py
"""
    Creates a token from a backtick quoted string.

    Moves the token_generator forwards till right after the next backtick.

    Parameters
    ----------
    token_generator : Iterator[tokenize.TokenInfo]
        The generator that yields the tokens of the source string (Tuple[int, str]).
        The generator is at the first token after the backtick (`)

    source : str
        The Python source code string.

    string_start : int
        This is the start of backtick quoted string inside the source string.

    Returns
    -------
    tok: Tuple[int, str]
        The token that represents the backtick quoted string.
        The integer is equal to BACKTICK_QUOTED_STRING (100).
    """
for _, tokval, start, _, _ in token_generator:
    if tokval == "`":
        string_end = start[1]
        break

exit((BACKTICK_QUOTED_STRING, source[string_start:string_end]))
