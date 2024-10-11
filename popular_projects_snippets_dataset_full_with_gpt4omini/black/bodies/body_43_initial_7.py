from typing import Set, Any # pragma: no cover

mode = type('MockMode', (object,), {'preview': True})() # pragma: no cover
FMT_OFF = {'# fmt: off'} # pragma: no cover
features = {} # pragma: no cover
parens_after = {'value1', 'value2'} # pragma: no cover
_maybe_wrap_cms_in_parens = lambda node, mode, features: None # pragma: no cover
normalize_invisible_parens = lambda child, parens_after, mode, features: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Make existing optional parentheses invisible or create new ones.

    `parens_after` is a set of string leaf values immediately after which parens
    should be put.

    Standardizes on visible parentheses for single-element tuples, and keeps
    existing visible parentheses for other tuples and generator expressions.
    """
for pc in list_comments(node.prefix, is_endmarker=False, preview=mode.preview):
    _l_(5942)

    if pc.value in FMT_OFF:
        _l_(5941)

        # This `node` has a prefix with `# fmt: off`, don't mess with parens.
        exit()
        _l_(5940)
if node.type == syms.with_stmt:
    _l_(5944)

    _maybe_wrap_cms_in_parens(node, mode, features)
    _l_(5943)

check_lpar = False
_l_(5945)
for index, child in enumerate(list(node.children)):
    _l_(5970)

    # Fixes a bug where invisible parens are not properly stripped from
    # assignment statements that contain type annotations.
    if isinstance(child, Node) and child.type == syms.annassign:
        _l_(5947)

        normalize_invisible_parens(
            child, parens_after=parens_after, mode=mode, features=features
        )
        _l_(5946)

    # Add parentheses around long tuple unpacking in assignments.
    if (
        index == 0
        and isinstance(child, Node)
        and child.type == syms.testlist_star_expr
    ):
        _l_(5949)

        check_lpar = True
        _l_(5948)

    if check_lpar:
        _l_(5967)

        if (
            mode.preview
            and child.type == syms.atom
            and node.type == syms.for_stmt
            and isinstance(child.prev_sibling, Leaf)
            and child.prev_sibling.type == token.NAME
            and child.prev_sibling.value == "for"
        ):
            _l_(5966)

            if maybe_make_parens_invisible_in_atom(
                child,
                parent=node,
                remove_brackets_around_comma=True,
            ):
                _l_(5951)

                wrap_in_parentheses(node, child, visible=False)
                _l_(5950)
        elif (
            mode.preview and isinstance(child, Node) and node.type == syms.with_stmt
        ):
            _l_(5965)

            remove_with_parens(child, node)
            _l_(5952)
        elif child.type == syms.atom:
            _l_(5964)

            if maybe_make_parens_invisible_in_atom(
                child,
                parent=node,
            ):
                _l_(5954)

                wrap_in_parentheses(node, child, visible=False)
                _l_(5953)
        elif is_one_tuple(child):
            _l_(5963)

            wrap_in_parentheses(node, child, visible=True)
            _l_(5955)
        elif node.type == syms.import_from:
            _l_(5962)

            _normalize_import_from(node, child, index)
            _l_(5956)
            break
            _l_(5957)
        elif (
            index == 1
            and child.type == token.STAR
            and node.type == syms.except_clause
        ):
            _l_(5961)

            # In except* (PEP 654), the star is actually part of
            # of the keyword. So we need to skip the insertion of
            # invisible parentheses to work more precisely.
            continue
            _l_(5958)

        elif not (isinstance(child, Leaf) and is_multiline_string(child)):
            _l_(5960)

            wrap_in_parentheses(node, child, visible=False)
            _l_(5959)

    comma_check = child.type == token.COMMA if mode.preview else False
    _l_(5968)

    check_lpar = isinstance(child, Leaf) and (
        child.value in parens_after or comma_check
    )
    _l_(5969)
