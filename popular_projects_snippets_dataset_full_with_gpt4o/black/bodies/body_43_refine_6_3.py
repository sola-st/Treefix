from typing import Set, List # pragma: no cover
from collections import namedtuple # pragma: no cover

list_comments = lambda prefix, is_endmarker, preview: [] # pragma: no cover
node = type('MockNode', (object,), {'prefix': '', 'type': None, 'children': [], 'prev_sibling': None})() # pragma: no cover
mode = type('MockMode', (object,), {'preview': False})() # pragma: no cover
FMT_OFF = set() # pragma: no cover
_maybe_wrap_cms_in_parens = lambda node, mode, features: None # pragma: no cover
features = {} # pragma: no cover
Node = namedtuple('Node', ['type', 'children', 'prev_sibling']) # pragma: no cover
normalize_invisible_parens = lambda *args, **kwargs: None # pragma: no cover
parens_after = set() # pragma: no cover
Leaf = namedtuple('Leaf', ['type', 'value']) # pragma: no cover
token = type('MockToken', (object,), {'NAME': 1, 'STAR': 2, 'COMMA': 3})() # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda *args, **kwargs: False # pragma: no cover
wrap_in_parentheses = lambda *args, **kwargs: None # pragma: no cover
remove_with_parens = lambda child, node: None # pragma: no cover
is_one_tuple = lambda child: False # pragma: no cover
is_multiline_string = lambda child: False # pragma: no cover

from typing import List, Set, Any # pragma: no cover
from types import SimpleNamespace # pragma: no cover
import token # pragma: no cover

list_comments = lambda *args, **kwargs: [] # pragma: no cover
node = SimpleNamespace(prefix='', type=1, children=[], prev_sibling=None) # pragma: no cover
mode = SimpleNamespace(preview=False) # pragma: no cover
FMT_OFF = set() # pragma: no cover
_maybe_wrap_cms_in_parens = lambda node, mode, features: None # pragma: no cover
features = set() # pragma: no cover
Node = SimpleNamespace # pragma: no cover
normalize_invisible_parens = lambda *args, **kwargs: None # pragma: no cover
parens_after = set() # pragma: no cover
Leaf = SimpleNamespace # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda *args, **kwargs: False # pragma: no cover
wrap_in_parentheses = lambda *args, **kwargs: None # pragma: no cover
remove_with_parens = lambda *args, **kwargs: None # pragma: no cover
is_one_tuple = lambda *args, **kwargs: False # pragma: no cover
is_multiline_string = lambda *args, **kwargs: False # pragma: no cover

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
