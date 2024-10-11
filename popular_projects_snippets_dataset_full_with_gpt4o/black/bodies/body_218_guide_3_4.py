from typing import Optional # pragma: no cover
import token # pragma: no cover

class LN: # pragma: no cover
    def __init__(self, type_val, children=None, next_sibling=None): # pragma: no cover
        self.type = type_val # pragma: no cover
        self.children = children if children else [] # pragma: no cover
        self.next_sibling = next_sibling # pragma: no cover
 # pragma: no cover
class Leaf(LN): # pragma: no cover
    def __init__(self, type_val, value=''): # pragma: no cover
        super().__init__(type_val) # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
leaf = Leaf(token.NAME, 'leaf_value') # pragma: no cover
comment = Leaf(token.COMMENT, '# fmt: skip') # pragma: no cover
FMT_SKIP = {'# fmt: skip'} # pragma: no cover
def _generate_ignored_nodes_from_fmt_skip(leaf, comment, preview=None): # pragma: no cover
    return [leaf] # pragma: no cover
def container_of(leaf): # pragma: no cover
    return LN(token.INDENT, children=[Leaf(token.INDENT), Leaf(token.DEDENT), Leaf(token.RBRACKET)], next_sibling=None) # pragma: no cover
def is_fmt_on(node, preview=None): # pragma: no cover
    return False # pragma: no cover
def children_contains_fmt_on(node, preview=None): # pragma: no cover
    return any(child.value == '# fmt: on' for child in node.children) # pragma: no cover
preview = False # pragma: no cover

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
