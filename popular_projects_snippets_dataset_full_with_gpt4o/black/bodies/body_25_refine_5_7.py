import re # pragma: no cover

import re # pragma: no cover

class PreviewOptions:# pragma: no cover
    hex_codes_in_unicode_sequences = 'hex_codes_in_unicode_sequences'# pragma: no cover
    normalize_docstring_quotes_and_prefixes_properly = 'normalize_docstring_quotes_and_prefixes_properly'# pragma: no cover
    long_docstring_quotes_on_newline = 'long_docstring_quotes_on_newline'# pragma: no cover
# pragma: no cover
class Mode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.options = [# pragma: no cover
            PreviewOptions.hex_codes_in_unicode_sequences,# pragma: no cover
            PreviewOptions.normalize_docstring_quotes_and_prefixes_properly,# pragma: no cover
            PreviewOptions.long_docstring_quotes_on_newline# pragma: no cover
        ]# pragma: no cover
        self.string_normalization = True# pragma: no cover
        self.line_length = 80# pragma: no cover
# pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value # pragma: no cover
def normalize_unicode_escape_sequences(leaf):# pragma: no cover
    pass # pragma: no cover
leaf = Leaf('"""This is a docstring"""') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
if Preview.hex_codes_in_unicode_sequences in self.mode:
    _l_(17931)

    normalize_unicode_escape_sequences(leaf)
    _l_(17930)

if is_docstring(leaf) and "\\\n" not in leaf.value:
    _l_(17969)

    # We're ignoring docstrings with backslash newline escapes because changing
    # indentation of those changes the AST representation of the code.
    if Preview.normalize_docstring_quotes_and_prefixes_properly in self.mode:
        _l_(17937)

        # There was a bug where --skip-string-normalization wouldn't stop us
        # from normalizing docstring prefixes. To maintain stability, we can
        # only address this buggy behaviour while the preview style is enabled.
        if self.mode.string_normalization:
            _l_(17935)

            docstring = normalize_string_prefix(leaf.value)
            _l_(17932)
            # visit_default() does handle string normalization for us, but
            # since this method acts differently depending on quote style (ex.
            # see padding logic below), there's a possibility for unstable
            # formatting as visit_default() is called *after*. To avoid a
            # situation where this function formats a docstring differently on
            # the second pass, normalize it early.
            docstring = normalize_string_quotes(docstring)
            _l_(17933)
        else:
            docstring = leaf.value
            _l_(17934)
    else:
        # ... otherwise, we'll keep the buggy behaviour >.<
        docstring = normalize_string_prefix(leaf.value)
        _l_(17936)
    prefix = get_string_prefix(docstring)
    _l_(17938)
    docstring = docstring[len(prefix) :]  # Remove the prefix
    _l_(17939)  # Remove the prefix
    quote_char = docstring[0]
    _l_(17940)
    # A natural way to remove the outer quotes is to do:
    #   docstring = docstring.strip(quote_char)
    # but that breaks on """""x""" (which is '""x').
    # So we actually need to remove the first character and the next two
    # characters but only if they are the same as the first.
    quote_len = 1 if docstring[1] != quote_char else 3
    _l_(17941)
    docstring = docstring[quote_len:-quote_len]
    _l_(17942)
    docstring_started_empty = not docstring
    _l_(17943)
    indent = " " * 4 * self.current_line.depth
    _l_(17944)

    if is_multiline_string(leaf):
        _l_(17947)

        docstring = fix_docstring(docstring, indent)
        _l_(17945)
    else:
        docstring = docstring.strip()
        _l_(17946)

    has_trailing_backslash = False
    _l_(17948)
    if docstring:
        _l_(17960)

        # Add some padding if the docstring starts / ends with a quote mark.
        if docstring[0] == quote_char:
            _l_(17950)

            docstring = " " + docstring
            _l_(17949)
        if docstring[-1] == quote_char:
            _l_(17952)

            docstring += " "
            _l_(17951)
        if docstring[-1] == "\\":
            _l_(17957)

            backslash_count = len(docstring) - len(docstring.rstrip("\\"))
            _l_(17953)
            if backslash_count % 2:
                _l_(17956)

                # Odd number of tailing backslashes, add some padding to
                # avoid escaping the closing string quote.
                docstring += " "
                _l_(17954)
                has_trailing_backslash = True
                _l_(17955)
    elif not docstring_started_empty:
        _l_(17959)

        docstring = " "
        _l_(17958)

    # We could enforce triple quotes at this point.
    quote = quote_char * quote_len
    _l_(17961)

    # It's invalid to put closing single-character quotes on a new line.
    if Preview.long_docstring_quotes_on_newline in self.mode and quote_len == 3:
        _l_(17968)

        # We need to find the length of the last line of the docstring
        # to find if we can add the closing quotes to the line without
        # exceeding the maximum line length.
        # If docstring is one line, we don't put the closing quotes on a
        # separate line because it looks ugly (#3320).
        lines = docstring.splitlines()
        _l_(17962)
        last_line_length = len(lines[-1]) if docstring else 0
        _l_(17963)

        # If adding closing quotes would cause the last line to exceed
        # the maximum line length then put a line break before the
        # closing quotes
        if (
            len(lines) > 1
            and last_line_length + quote_len > self.mode.line_length
            and len(indent) + quote_len <= self.mode.line_length
            and not has_trailing_backslash
        ):
            _l_(17966)

            leaf.value = prefix + quote + docstring + "\n" + indent + quote
            _l_(17964)
        else:
            leaf.value = prefix + quote + docstring + quote
            _l_(17965)
    else:
        leaf.value = prefix + quote + docstring + quote
        _l_(17967)
aux = self.visit_default(leaf)
_l_(17970)

exit(aux)
