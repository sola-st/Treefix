import token # pragma: no cover
from typing import Set # pragma: no cover
from blib2to3.pytree import Leaf, Node # pragma: no cover

def list_comments(prefix, is_endmarker=False, preview=False): # pragma: no cover
    return [Leaf(token.COMMENT, '# some_comment')] # pragma: no cover
 # pragma: no cover
FMT_OFF = {'# fmt: off'} # pragma: no cover
 # pragma: no cover
class MockMode: # pragma: no cover
    preview = True # pragma: no cover
mode = MockMode() # pragma: no cover
 # pragma: no cover
parens_after = {'example'} # pragma: no cover
features = set() # pragma: no cover
 # pragma: no cover
def _maybe_wrap_cms_in_parens(node, mode, features): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
def normalize_invisible_parens(child, parens_after, mode, features): # pragma: no cover
    print('normalize_invisible_parens executed') # pragma: no cover
 # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma=False): # pragma: no cover
    print('maybe_make_parens_invisible_in_atom executed') # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
def wrap_in_parentheses(node, child, visible): # pragma: no cover
    print('wrap_in_parentheses executed') # pragma: no cover
 # pragma: no cover
def remove_with_parens(child, node): # pragma: no cover
    print('remove_with_parens executed') # pragma: no cover
 # pragma: no cover
def is_one_tuple(child): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
 # pragma: no cover
def is_multiline_string(child): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
leaf_for = Leaf(token.NAME, 'for') # pragma: no cover

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
    _l_(17445)

    if pc.value in FMT_OFF:
        _l_(17444)

        # This `node` has a prefix with `# fmt: off`, don't mess with parens.
        exit()
        _l_(17443)
if node.type == syms.with_stmt:
    _l_(17447)

    _maybe_wrap_cms_in_parens(node, mode, features)
    _l_(17446)

check_lpar = False
_l_(17448)
for index, child in enumerate(list(node.children)):
    _l_(17473)

    # Fixes a bug where invisible parens are not properly stripped from
    # assignment statements that contain type annotations.
    if isinstance(child, Node) and child.type == syms.annassign:
        _l_(17450)

        normalize_invisible_parens(
            child, parens_after=parens_after, mode=mode, features=features
        )
        _l_(17449)

    # Add parentheses around long tuple unpacking in assignments.
    if (
        index == 0
        and isinstance(child, Node)
        and child.type == syms.testlist_star_expr
    ):
        _l_(17452)

        check_lpar = True
        _l_(17451)

    if check_lpar:
        _l_(17470)

        if (
            mode.preview
            and child.type == syms.atom
            and node.type == syms.for_stmt
            and isinstance(child.prev_sibling, Leaf)
            and child.prev_sibling.type == token.NAME
            and child.prev_sibling.value == "for"
        ):
            _l_(17469)

            if maybe_make_parens_invisible_in_atom(
                child,
                parent=node,
                remove_brackets_around_comma=True,
            ):
                _l_(17454)

                wrap_in_parentheses(node, child, visible=False)
                _l_(17453)
        elif (
            mode.preview and isinstance(child, Node) and node.type == syms.with_stmt
        ):
            _l_(17468)

            remove_with_parens(child, node)
            _l_(17455)
        elif child.type == syms.atom:
            _l_(17467)

            if maybe_make_parens_invisible_in_atom(
                child,
                parent=node,
            ):
                _l_(17457)

                wrap_in_parentheses(node, child, visible=False)
                _l_(17456)
        elif is_one_tuple(child):
            _l_(17466)

            wrap_in_parentheses(node, child, visible=True)
            _l_(17458)
        elif node.type == syms.import_from:
            _l_(17465)

            _normalize_import_from(node, child, index)
            _l_(17459)
            break
            _l_(17460)
        elif (
            index == 1
            and child.type == token.STAR
            and node.type == syms.except_clause
        ):
            _l_(17464)

            # In except* (PEP 654), the star is actually part of
            # of the keyword. So we need to skip the insertion of
            # invisible parentheses to work more precisely.
            continue
            _l_(17461)

        elif not (isinstance(child, Leaf) and is_multiline_string(child)):
            _l_(17463)

            wrap_in_parentheses(node, child, visible=False)
            _l_(17462)

    comma_check = child.type == token.COMMA if mode.preview else False
    _l_(17471)

    check_lpar = isinstance(child, Leaf) and (
        child.value in parens_after or comma_check
    )
    _l_(17472)
