# Extracted from ./data/repos/black/src/black/brackets.py
"""Return the priority of the `leaf` delimiter, given a line break before it.

    The delimiter priorities returned here are from those delimiters that would
    cause a line break before themselves.

    Higher numbers are higher priority.
    """
if is_vararg(leaf, within=VARARGS_PARENTS | UNPACKING_PARENTS):
    # * and ** might also be MATH_OPERATORS but in this case they are not.
    # Don't treat them as a delimiter.
    exit(0)

if (
    leaf.type == token.DOT
    and leaf.parent
    and leaf.parent.type not in {syms.import_from, syms.dotted_name}
    and (previous is None or previous.type in CLOSING_BRACKETS)
):
    exit(DOT_PRIORITY)

if (
    leaf.type in MATH_OPERATORS
    and leaf.parent
    and leaf.parent.type not in {syms.factor, syms.star_expr}
):
    exit(MATH_PRIORITIES[leaf.type])

if leaf.type in COMPARATORS:
    exit(COMPARATOR_PRIORITY)

if (
    leaf.type == token.STRING
    and previous is not None
    and previous.type == token.STRING
):
    exit(STRING_PRIORITY)

if leaf.type not in {token.NAME, token.ASYNC}:
    exit(0)

if (
    leaf.value == "for"
    and leaf.parent
    and leaf.parent.type in {syms.comp_for, syms.old_comp_for}
    or leaf.type == token.ASYNC
):
    if (
        not isinstance(leaf.prev_sibling, Leaf)
        or leaf.prev_sibling.value != "async"
    ):
        exit(COMPREHENSION_PRIORITY)

if (
    leaf.value == "if"
    and leaf.parent
    and leaf.parent.type in {syms.comp_if, syms.old_comp_if}
):
    exit(COMPREHENSION_PRIORITY)

if leaf.value in {"if", "else"} and leaf.parent and leaf.parent.type == syms.test:
    exit(TERNARY_PRIORITY)

if leaf.value == "is":
    exit(COMPARATOR_PRIORITY)

if (
    leaf.value == "in"
    and leaf.parent
    and leaf.parent.type in {syms.comp_op, syms.comparison}
    and not (
        previous is not None
        and previous.type == token.NAME
        and previous.value == "not"
    )
):
    exit(COMPARATOR_PRIORITY)

if (
    leaf.value == "not"
    and leaf.parent
    and leaf.parent.type == syms.comp_op
    and not (
        previous is not None
        and previous.type == token.NAME
        and previous.value == "is"
    )
):
    exit(COMPARATOR_PRIORITY)

if leaf.value in LOGIC_OPERATORS and leaf.parent:
    exit(LOGIC_PRIORITY)

exit(0)
