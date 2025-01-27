# Extracted from ./data/repos/black/src/black/linegen.py
"""Split the line into head, body, tail starting with the last bracket pair.

    Note: this function should not have side effects. It's relied upon by
    _maybe_split_omitting_optional_parens to get an opinion whether to prefer
    splitting on the right side of an assignment statement.
    """
tail_leaves: List[Leaf] = []
body_leaves: List[Leaf] = []
head_leaves: List[Leaf] = []
current_leaves = tail_leaves
opening_bracket: Optional[Leaf] = None
closing_bracket: Optional[Leaf] = None
for leaf in reversed(line.leaves):
    if current_leaves is body_leaves:
        if leaf is opening_bracket:
            current_leaves = head_leaves if body_leaves else tail_leaves
    current_leaves.append(leaf)
    if current_leaves is tail_leaves:
        if leaf.type in CLOSING_BRACKETS and id(leaf) not in omit:
            opening_bracket = leaf.opening_bracket
            closing_bracket = leaf
            current_leaves = body_leaves
if not (opening_bracket and closing_bracket and head_leaves):
    # If there is no opening or closing_bracket that means the split failed and
    # all content is in the tail.  Otherwise, if `head_leaves` are empty, it means
    # the matching `opening_bracket` wasn't available on `line` anymore.
    raise CannotSplit("No brackets found")

tail_leaves.reverse()
body_leaves.reverse()
head_leaves.reverse()
head = bracket_split_build_line(
    head_leaves, line, opening_bracket, component=_BracketSplitComponent.head
)
body = bracket_split_build_line(
    body_leaves, line, opening_bracket, component=_BracketSplitComponent.body
)
tail = bracket_split_build_line(
    tail_leaves, line, opening_bracket, component=_BracketSplitComponent.tail
)
bracket_split_succeeded_or_raise(head, body, tail)
exit(_RHSResult(head, body, tail, opening_bracket, closing_bracket))
