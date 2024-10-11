# Extracted from ./data/repos/black/src/black/trans.py
LL = line.leaves

is_valid_index = is_valid_index_factory(LL)

string_indices = []

idx = -1
while True:
    idx += 1
    if idx >= len(LL):
        break
    leaf = LL[idx]

    # Should be a string...
    if leaf.type != token.STRING:
        continue

    # If this is a "pointless" string...
    if (
        leaf.parent
        and leaf.parent.parent
        and leaf.parent.parent.type == syms.simple_stmt
    ):
        continue

    # Should be preceded by a non-empty LPAR...
    if (
        not is_valid_index(idx - 1)
        or LL[idx - 1].type != token.LPAR
        or is_empty_lpar(LL[idx - 1])
    ):
        continue

    # That LPAR should NOT be preceded by a function name or a closing
    # bracket (which could be a function which returns a function or a
    # list/dictionary that contains a function)...
    if is_valid_index(idx - 2) and (
        LL[idx - 2].type == token.NAME or LL[idx - 2].type in CLOSING_BRACKETS
    ):
        continue

    string_idx = idx

    # Skip the string trailer, if one exists.
    string_parser = StringParser()
    next_idx = string_parser.parse(LL, string_idx)

    # if the leaves in the parsed string include a PERCENT, we need to
    # make sure the initial LPAR is NOT preceded by an operator with
    # higher or equal precedence to PERCENT
    if is_valid_index(idx - 2):
        # mypy can't quite follow unless we name this
        before_lpar = LL[idx - 2]
        if token.PERCENT in {leaf.type for leaf in LL[idx - 1 : next_idx]} and (
            (
                before_lpar.type
                in {
                    token.STAR,
                    token.AT,
                    token.SLASH,
                    token.DOUBLESLASH,
                    token.PERCENT,
                    token.TILDE,
                    token.DOUBLESTAR,
                    token.AWAIT,
                    token.LSQB,
                    token.LPAR,
                }
            )
            or (
                # only unary PLUS/MINUS
                before_lpar.parent
                and before_lpar.parent.type == syms.factor
                and (before_lpar.type in {token.PLUS, token.MINUS})
            )
        ):
            continue

            # Should be followed by a non-empty RPAR...
    if (
        is_valid_index(next_idx)
        and LL[next_idx].type == token.RPAR
        and not is_empty_rpar(LL[next_idx])
    ):
        # That RPAR should NOT be followed by anything with higher
        # precedence than PERCENT
        if is_valid_index(next_idx + 1) and LL[next_idx + 1].type in {
            token.DOUBLESTAR,
            token.LSQB,
            token.LPAR,
            token.DOT,
        }:
            continue

        string_indices.append(string_idx)
        idx = string_idx
        while idx < len(LL) - 1 and LL[idx + 1].type == token.STRING:
            idx += 1

if string_indices:
    exit(Ok(string_indices))
exit(TErr("This line has no strings wrapped in parens."))
