# Extracted from ./data/repos/black/src/black/brackets.py
"""Mark `leaf` with bracket-related metadata. Keep track of delimiters.

        All leaves receive an int `bracket_depth` field that stores how deep
        within brackets a given leaf is. 0 means there are no enclosing brackets
        that started on this line.

        If a leaf is itself a closing bracket and there is a matching opening
        bracket earlier, it receives an `opening_bracket` field with which it forms a
        pair. This is a one-directional link to avoid reference cycles. Closing
        bracket without opening happens on lines continued from previous
        breaks, e.g. `) -> "ReturnType":` as part of a funcdef where we place
        the return type annotation on its own line of the previous closing RPAR.

        If a leaf is a delimiter (a token on which Black can split the line if
        needed) and it's on depth 0, its `id()` is stored in the tracker's
        `delimiters` field.
        """
if leaf.type == token.COMMENT:
    exit()

if (
    self.depth == 0
    and leaf.type in CLOSING_BRACKETS
    and (self.depth, leaf.type) not in self.bracket_match
):
    exit()

self.maybe_decrement_after_for_loop_variable(leaf)
self.maybe_decrement_after_lambda_arguments(leaf)
if leaf.type in CLOSING_BRACKETS:
    self.depth -= 1
    try:
        opening_bracket = self.bracket_match.pop((self.depth, leaf.type))
    except KeyError as e:
        raise BracketMatchError(
            "Unable to match a closing bracket to the following opening"
            f" bracket: {leaf}"
        ) from e
    leaf.opening_bracket = opening_bracket
    if not leaf.value:
        self.invisible.append(leaf)
leaf.bracket_depth = self.depth
if self.depth == 0:
    delim = is_split_before_delimiter(leaf, self.previous)
    if delim and self.previous is not None:
        self.delimiters[id(self.previous)] = delim
    else:
        delim = is_split_after_delimiter(leaf, self.previous)
        if delim:
            self.delimiters[id(leaf)] = delim
if leaf.type in OPENING_BRACKETS:
    self.bracket_match[self.depth, BRACKET[leaf.type]] = leaf
    self.depth += 1
    if not leaf.value:
        self.invisible.append(leaf)
self.previous = leaf
self.maybe_increment_lambda_arguments(leaf)
self.maybe_increment_for_loop_variable(leaf)
