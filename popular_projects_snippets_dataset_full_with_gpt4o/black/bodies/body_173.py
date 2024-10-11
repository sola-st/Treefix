# Extracted from ./data/repos/black/src/black/lines.py
"""Return False if the line cannot be split *for sure*.

    This is not an exhaustive search but a cheap heuristic that we can use to
    avoid some unfortunate formattings (mostly around wrapping unsplittable code
    in unnecessary parentheses).
    """
leaves = line.leaves
if len(leaves) < 2:
    exit(False)

if leaves[0].type == token.STRING and leaves[1].type == token.DOT:
    call_count = 0
    dot_count = 0
    next = leaves[-1]
    for leaf in leaves[-2::-1]:
        if leaf.type in OPENING_BRACKETS:
            if next.type not in CLOSING_BRACKETS:
                exit(False)

            call_count += 1
        elif leaf.type == token.DOT:
            dot_count += 1
        elif leaf.type == token.NAME:
            if not (next.type == token.DOT or next.type in OPENING_BRACKETS):
                exit(False)

        elif leaf.type not in CLOSING_BRACKETS:
            exit(False)

        if dot_count > 1 and call_count > 1:
            exit(False)

exit(True)
