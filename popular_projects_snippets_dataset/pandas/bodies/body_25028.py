# Extracted from ./data/repos/pandas/pandas/io/formats/printing.py
translate = {"\t": r"\t", "\n": r"\n", "\r": r"\r"}
if isinstance(escape_chars, dict):
    if default_escapes:
        translate.update(escape_chars)
    else:
        translate = escape_chars
    escape_chars = list(escape_chars.keys())
else:
    escape_chars = escape_chars or ()

result = str(thing)
for c in escape_chars:
    result = result.replace(c, translate[c])
exit(result)
