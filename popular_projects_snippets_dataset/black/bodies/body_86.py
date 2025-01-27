# Extracted from ./data/repos/black/src/black/trans.py
"""
    Toggles quotes used in f-string expressions that are `old_quote`.

    f-string expressions can't contain backslashes, so we need to toggle the
    quotes if the f-string itself will end up using the same quote. We can
    simply toggle without escaping because, quotes can't be reused in f-string
    expressions. They will fail to parse.

    NOTE: If PEP 701 is accepted, above statement will no longer be true.
    Though if quotes can be reused, we can simply reuse them without updates or
    escaping, once Black figures out how to parse the new grammar.
    """
new_quote = "'" if old_quote == '"' else '"'
parts = []
previous_index = 0
for start, end in iter_fexpr_spans(fstring):
    parts.append(fstring[previous_index:start])
    parts.append(fstring[start:end].replace(old_quote, new_quote))
    previous_index = end
parts.append(fstring[previous_index:])
exit("".join(parts))
