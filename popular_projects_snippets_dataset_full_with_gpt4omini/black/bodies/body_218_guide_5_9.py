from typing import Optional # pragma: no cover
import token # pragma: no cover

class Leaf: pass # pragma: no cover
class MockNode:  # mock for nodes in the tree # pragma: no cover
    def __init__(self, node_type, children=None, next_sibling=None): # pragma: no cover
        self.type = node_type # pragma: no cover
        self.children = children if children is not None else [] # pragma: no cover
        self.next_sibling = next_sibling # pragma: no cover
FMT_SKIP = ['skip'] # pragma: no cover
def _generate_ignored_nodes_from_fmt_skip(leaf, comment, preview): return 'ignored_nodes' # pragma: no cover
leaf = Leaf() # pragma: no cover
comment = type('MockComment', (object,), {'value': 'skip'})() # pragma: no cover
preview = None # pragma: no cover
container = MockNode(token.ENDMARKER, children=[leaf]) # pragma: no cover
child_node = MockNode(token.STRING, children=[], next_sibling=None) # pragma: no cover
child_node.value = '# fmt: on' # pragma: no cover
container.children.append(child_node) # pragma: no cover
def container_of(leaf): return container # pragma: no cover
def is_fmt_on(node, preview): return node.value == '# fmt: on' # pragma: no cover
def children_contains_fmt_on(container, preview): return True # pragma: no cover
CLOSING_BRACKETS = [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Starting from the container of `leaf`, generate all leaves until `# fmt: on`.

    If comment is skip, returns leaf only.
    Stops at the end of the block.
    """
if comment.value in FMT_SKIP:
    _l_(5235)

    aux = _generate_ignored_nodes_from_fmt_skip(leaf, comment, preview=preview)
    _l_(5233)
    exit(aux)
    exit()
    _l_(5234)
container: Optional[LN] = container_of(leaf)
_l_(5236)
while container is not None and container.type != token.ENDMARKER:
    _l_(5254)

    if is_fmt_on(container, preview=preview):
        _l_(5238)

        exit()
        _l_(5237)

    # fix for fmt: on in children
    if children_contains_fmt_on(container, preview=preview):
        _l_(5253)

        for index, child in enumerate(container.children):
            _l_(5248)

            if isinstance(child, Leaf) and is_fmt_on(child, preview=preview):
                _l_(5242)

                if child.type in CLOSING_BRACKETS:
                    _l_(5240)

                    aux = child
                    _l_(5239)
                    # This means `# fmt: on` is placed at a different bracket level
                    # than `# fmt: off`. This is an invalid use, but as a courtesy,
                    # we include this closing bracket in the ignored nodes.
                    # The alternative is to fail the formatting.
                    exit(aux)
                exit()
                _l_(5241)
            if (
                child.type == token.INDENT
                and index < len(container.children) - 1
                and children_contains_fmt_on(
                    container.children[index + 1], preview=preview
                )
            ):
                _l_(5244)

                # This means `# fmt: on` is placed right after an indentation
                # level, and we shouldn't swallow the previous INDENT token.
                exit()
                _l_(5243)
            if children_contains_fmt_on(child, preview=preview):
                _l_(5246)

                exit()
                _l_(5245)
            aux = child
            _l_(5247)
            exit(aux)
    else:
        if container.type == token.DEDENT and container.next_sibling is None:
            _l_(5250)

            # This can happen when there is no matching `# fmt: on` comment at the
            # same level as `# fmt: on`. We need to keep this DEDENT.
            exit()
            _l_(5249)
        aux = container
        _l_(5251)
        exit(aux)
        container = container.next_sibling
        _l_(5252)
