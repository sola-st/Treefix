from typing import Optional # pragma: no cover
import token # pragma: no cover

comment = type('Mock', (object,), {'value': '# fmt: off'})() # pragma: no cover
FMT_SKIP = set(['skip_comment']) # pragma: no cover
_generate_ignored_nodes_from_fmt_skip = lambda leaf, comment, preview: None # pragma: no cover
leaf = type('Mock', (object,), {'value': 'leaf_value'})() # pragma: no cover
preview = False # pragma: no cover
LN = object # pragma: no cover
container_of = lambda leaf: type('Mock', (object,), {'type': token.INDENT, 'children': [], 'next_sibling': None})() # pragma: no cover
token.ENDMARKER = 0 # pragma: no cover
token.INDENT = 1 # pragma: no cover
token.DEDENT = 2 # pragma: no cover
is_fmt_on = lambda node, preview: False # pragma: no cover
children_contains_fmt_on = lambda node, preview: False # pragma: no cover
Leaf = type('Mock', (object,), {}) # pragma: no cover
CLOSING_BRACKETS = set([')', '}', ']']) # pragma: no cover

from typing import Optional # pragma: no cover
import token # pragma: no cover

comment = type('Mock', (object,), {'value': '# fmt: off'})() # pragma: no cover
FMT_SKIP = {'# fmt: off'} # pragma: no cover
_generate_ignored_nodes_from_fmt_skip = lambda leaf, comment, preview: None # pragma: no cover
leaf = type('MockLeaf', (object,), {'type': 1, 'value': 'leaf_value'})() # pragma: no cover
preview = False # pragma: no cover
LN = type('MockLN', (object,), {}) # pragma: no cover
container_of = lambda leaf: type('MockContainer', (object,), {'type': 1, 'children': [], 'next_sibling': None})() # pragma: no cover
is_fmt_on = lambda node, preview: node.type == 3 # pragma: no cover
children_contains_fmt_on = lambda node, preview: any(child.type == 3 for child in node.children) if hasattr(node, 'children') else False # pragma: no cover
Leaf = type('MockLeaf', (object,), {'type': None, 'value': ''}) # pragma: no cover
CLOSING_BRACKETS = {')', '}', ']'} # pragma: no cover
token = type('MockToken', (object,), {'ENDMARKER': 0, 'INDENT': 1, 'DEDENT': 2})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Starting from the container of `leaf`, generate all leaves until `# fmt: on`.

    If comment is skip, returns leaf only.
    Stops at the end of the block.
    """
if comment.value in FMT_SKIP:
    _l_(16789)

    aux = _generate_ignored_nodes_from_fmt_skip(leaf, comment, preview=preview)
    _l_(16787)
    exit(aux)
    exit()
    _l_(16788)
container: Optional[LN] = container_of(leaf)
_l_(16790)
while container is not None and container.type != token.ENDMARKER:
    _l_(16808)

    if is_fmt_on(container, preview=preview):
        _l_(16792)

        exit()
        _l_(16791)

    # fix for fmt: on in children
    if children_contains_fmt_on(container, preview=preview):
        _l_(16807)

        for index, child in enumerate(container.children):
            _l_(16802)

            if isinstance(child, Leaf) and is_fmt_on(child, preview=preview):
                _l_(16796)

                if child.type in CLOSING_BRACKETS:
                    _l_(16794)

                    aux = child
                    _l_(16793)
                    # This means `# fmt: on` is placed at a different bracket level
                    # than `# fmt: off`. This is an invalid use, but as a courtesy,
                    # we include this closing bracket in the ignored nodes.
                    # The alternative is to fail the formatting.
                    exit(aux)
                exit()
                _l_(16795)
            if (
                child.type == token.INDENT
                and index < len(container.children) - 1
                and children_contains_fmt_on(
                    container.children[index + 1], preview=preview
                )
            ):
                _l_(16798)

                # This means `# fmt: on` is placed right after an indentation
                # level, and we shouldn't swallow the previous INDENT token.
                exit()
                _l_(16797)
            if children_contains_fmt_on(child, preview=preview):
                _l_(16800)

                exit()
                _l_(16799)
            aux = child
            _l_(16801)
            exit(aux)
    else:
        if container.type == token.DEDENT and container.next_sibling is None:
            _l_(16804)

            # This can happen when there is no matching `# fmt: on` comment at the
            # same level as `# fmt: on`. We need to keep this DEDENT.
            exit()
            _l_(16803)
        aux = container
        _l_(16805)
        exit(aux)
        container = container.next_sibling
        _l_(16806)
