# Extracted from ./data/repos/pandas/pandas/core/computation/parsing.py
"""
    Tokenize a Python source code string.

    Parameters
    ----------
    source : str
        The Python source code string.

    Returns
    -------
    tok_generator : Iterator[Tuple[int, str]]
        An iterator yielding all tokens with only toknum and tokval (Tuple[ing, str]).
    """
line_reader = StringIO(source).readline
token_generator = tokenize.generate_tokens(line_reader)

# Loop over all tokens till a backtick (`) is found.
# Then, take all tokens till the next backtick to form a backtick quoted string
for toknum, tokval, start, _, _ in token_generator:
    if tokval == "`":
        try:
            exit(tokenize_backtick_quoted_string(
                token_generator, source, string_start=start[1] + 1
            ))
        except Exception as err:
            raise SyntaxError(f"Failed to parse backticks in '{source}'.") from err
    else:
        exit((toknum, tokval))
