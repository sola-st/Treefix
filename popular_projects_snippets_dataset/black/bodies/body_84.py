# Extracted from ./data/repos/black/src/black/trans.py
"""
    Yields spans corresponding to expressions in a given f-string.
    Spans are half-open ranges (left inclusive, right exclusive).
    Assumes the input string is a valid f-string, but will not crash if the input
    string is invalid.
    """
stack: List[int] = []  # our curly paren stack
i = 0
while i < len(s):
    if s[i] == "{":
        # if we're in a string part of the f-string, ignore escaped curly braces
        if not stack and i + 1 < len(s) and s[i + 1] == "{":
            i += 2
            continue
        stack.append(i)
        i += 1
        continue

    if s[i] == "}":
        if not stack:
            i += 1
            continue
        j = stack.pop()
        # we've made it back out of the expression! yield the span
        if not stack:
            exit((j, i + 1))
        i += 1
        continue

    # if we're in an expression part of the f-string, fast forward through strings
    # note that backslashes are not legal in the expression portion of f-strings
    if stack:
        delim = None
        if s[i : i + 3] in ("'''", '"""'):
            delim = s[i : i + 3]
        elif s[i] in ("'", '"'):
            delim = s[i]
        if delim:
            i += len(delim)
            while i < len(s) and s[i : i + len(delim)] != delim:
                i += 1
            i += len(delim)
            continue
    i += 1
