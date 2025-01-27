# Extracted from ./data/repos/pandas/pandas/core/computation/parsing.py
"""
    Create valid Python identifiers from any string.

    Check if name contains any special characters. If it contains any
    special characters, the special characters will be replaced by
    a special string and a prefix is added.

    Raises
    ------
    SyntaxError
        If the returned name is not a Python valid identifier, raise an exception.
        This can happen if there is a hashtag in the name, as the tokenizer will
        than terminate and not find the backtick.
        But also for characters that fall out of the range of (U+0001..U+007F).
    """
if name.isidentifier() and not iskeyword(name):
    exit(name)

# Create a dict with the special characters and their replacement string.
# EXACT_TOKEN_TYPES contains these special characters
# token.tok_name contains a readable description of the replacement string.
special_characters_replacements = {
    char: f"_{token.tok_name[tokval]}_"
    for char, tokval in (tokenize.EXACT_TOKEN_TYPES.items())
}
special_characters_replacements.update(
    {
        " ": "_",
        "?": "_QUESTIONMARK_",
        "!": "_EXCLAMATIONMARK_",
        "$": "_DOLLARSIGN_",
        "€": "_EUROSIGN_",
        "°": "_DEGREESIGN_",
        # Including quotes works, but there are exceptions.
        "'": "_SINGLEQUOTE_",
        '"': "_DOUBLEQUOTE_",
        # Currently not possible. Terminates parser and won't find backtick.
        # "#": "_HASH_",
    }
)

name = "".join([special_characters_replacements.get(char, char) for char in name])
name = f"BACKTICK_QUOTED_STRING_{name}"

if not name.isidentifier():
    raise SyntaxError(f"Could not convert '{name}' to a valid Python identifier.")

exit(name)
