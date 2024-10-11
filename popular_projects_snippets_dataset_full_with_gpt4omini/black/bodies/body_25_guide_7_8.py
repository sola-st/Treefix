from typing import Any # pragma: no cover

class Preview: # pragma: no cover
    hex_codes_in_unicode_sequences = 'enabled' # pragma: no cover
    normalize_docstring_quotes_and_prefixes_properly = 'enabled' # pragma: no cover
    long_docstring_quotes_on_newline = 'enabled' # pragma: no cover
 # pragma: no cover
class MockMode: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.string_normalization = True # pragma: no cover
        self.line_length = 50 # pragma: no cover
        self.mode = {Preview.hex_codes_in_unicode_sequences, Preview.normalize_docstring_quotes_and_prefixes_properly, Preview.long_docstring_quotes_on_newline} # pragma: no cover
 # pragma: no cover
class MockCurrentLine: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.depth = 1 # pragma: no cover
 # pragma: no cover
class MockLeaf: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.mode = MockMode() # pragma: no cover
        self.current_line = MockCurrentLine() # pragma: no cover
    def visit_default(self, leaf): return leaf.value # pragma: no cover
 # pragma: no cover
def normalize_unicode_escape_sequences(leaf: Any): pass # pragma: no cover
def is_docstring(leaf: Any) -> bool: return True # pragma: no cover
def normalize_string_prefix(value: str) -> str: return value # pragma: no cover
def normalize_string_quotes(value: str) -> str: return value # pragma: no cover
def get_string_prefix(value: str) -> str: return '' # pragma: no cover
def is_multiline_string(leaf: Any) -> bool: return True # pragma: no cover
def fix_docstring(docstring: str, indent: str) -> str: return docstring.strip() # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
leaf = MockLeaf('"""This is a multiline docstring with enough text to check wrapping."""') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
if Preview.hex_codes_in_unicode_sequences in self.mode:
    _l_(6451)

    normalize_unicode_escape_sequences(leaf)
    _l_(6450)

if is_docstring(leaf) and "\\\n" not in leaf.value:
    _l_(6489)

    # We're ignoring docstrings with backslash newline escapes because changing
    # indentation of those changes the AST representation of the code.
    if Preview.normalize_docstring_quotes_and_prefixes_properly in self.mode:
        _l_(6457)

        # There was a bug where --skip-string-normalization wouldn't stop us
        # from normalizing docstring prefixes. To maintain stability, we can
        # only address this buggy behaviour while the preview style is enabled.
        if self.mode.string_normalization:
            _l_(6455)

            docstring = normalize_string_prefix(leaf.value)
            _l_(6452)
            # visit_default() does handle string normalization for us, but
            # since this method acts differently depending on quote style (ex.
            # see padding logic below), there's a possibility for unstable
            # formatting as visit_default() is called *after*. To avoid a
            # situation where this function formats a docstring differently on
            # the second pass, normalize it early.
            docstring = normalize_string_quotes(docstring)
            _l_(6453)
        else:
            docstring = leaf.value
            _l_(6454)
    else:
        # ... otherwise, we'll keep the buggy behaviour >.<
        docstring = normalize_string_prefix(leaf.value)
        _l_(6456)
    prefix = get_string_prefix(docstring)
    _l_(6458)
    docstring = docstring[len(prefix) :]  # Remove the prefix
    _l_(6459)  # Remove the prefix
    quote_char = docstring[0]
    _l_(6460)
    # A natural way to remove the outer quotes is to do:
    #   docstring = docstring.strip(quote_char)
    # but that breaks on """""x""" (which is '""x').
    # So we actually need to remove the first character and the next two
    # characters but only if they are the same as the first.
    quote_len = 1 if docstring[1] != quote_char else 3
    _l_(6461)
    docstring = docstring[quote_len:-quote_len]
    _l_(6462)
    docstring_started_empty = not docstring
    _l_(6463)
    indent = " " * 4 * self.current_line.depth
    _l_(6464)

    if is_multiline_string(leaf):
        _l_(6467)

        docstring = fix_docstring(docstring, indent)
        _l_(6465)
    else:
        docstring = docstring.strip()
        _l_(6466)

    has_trailing_backslash = False
    _l_(6468)
    if docstring:
        _l_(6480)

        # Add some padding if the docstring starts / ends with a quote mark.
        if docstring[0] == quote_char:
            _l_(6470)

            docstring = " " + docstring
            _l_(6469)
        if docstring[-1] == quote_char:
            _l_(6472)

            docstring += " "
            _l_(6471)
        if docstring[-1] == "\\":
            _l_(6477)

            backslash_count = len(docstring) - len(docstring.rstrip("\\"))
            _l_(6473)
            if backslash_count % 2:
                _l_(6476)

                # Odd number of tailing backslashes, add some padding to
                # avoid escaping the closing string quote.
                docstring += " "
                _l_(6474)
                has_trailing_backslash = True
                _l_(6475)
    elif not docstring_started_empty:
        _l_(6479)

        docstring = " "
        _l_(6478)

    # We could enforce triple quotes at this point.
    quote = quote_char * quote_len
    _l_(6481)

    # It's invalid to put closing single-character quotes on a new line.
    if Preview.long_docstring_quotes_on_newline in self.mode and quote_len == 3:
        _l_(6488)

        # We need to find the length of the last line of the docstring
        # to find if we can add the closing quotes to the line without
        # exceeding the maximum line length.
        # If docstring is one line, we don't put the closing quotes on a
        # separate line because it looks ugly (#3320).
        lines = docstring.splitlines()
        _l_(6482)
        last_line_length = len(lines[-1]) if docstring else 0
        _l_(6483)

        # If adding closing quotes would cause the last line to exceed
        # the maximum line length then put a line break before the
        # closing quotes
        if (
            len(lines) > 1
            and last_line_length + quote_len > self.mode.line_length
            and len(indent) + quote_len <= self.mode.line_length
            and not has_trailing_backslash
        ):
            _l_(6486)

            leaf.value = prefix + quote + docstring + "\n" + indent + quote
            _l_(6484)
        else:
            leaf.value = prefix + quote + docstring + quote
            _l_(6485)
    else:
        leaf.value = prefix + quote + docstring + quote
        _l_(6487)
aux = self.visit_default(leaf)
_l_(6490)

exit(aux)
