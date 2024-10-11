from typing import List # pragma: no cover
import token # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, prefix='', prev_sibling=None, parent=None, node_type=None):# pragma: no cover
        self.prefix = prefix# pragma: no cover
        self.prev_sibling = prev_sibling# pragma: no cover
        self.parent = parent# pragma: no cover
        self.type = node_type # pragma: no cover
prev_sibling = MockNode(prefix='previous_prefix') # pragma: no cover
comment = type('Comment', (object,), {'value': 'some_prefix'})() # pragma: no cover
def list_comments(prefix, is_endmarker=False, preview=None): return [comment] # pragma: no cover
preview = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Generate all leaves that should be ignored by the `# fmt: skip` from `leaf`."""
prev_sibling = leaf.prev_sibling
_l_(7391)
parent = leaf.parent
_l_(7392)
# Need to properly format the leaf prefix to compare it to comment.value,
# which is also formatted
comments = list_comments(leaf.prefix, is_endmarker=False, preview=preview)
_l_(7393)
if not comments or comment.value != comments[0].value:
    _l_(7395)

    exit()
    _l_(7394)
if prev_sibling is not None:
    _l_(7413)

    leaf.prefix = ""
    _l_(7396)
    siblings = [prev_sibling]
    _l_(7397)
    while "\n" not in prev_sibling.prefix and prev_sibling.prev_sibling is not None:
        _l_(7400)

        prev_sibling = prev_sibling.prev_sibling
        _l_(7398)
        siblings.insert(0, prev_sibling)
        _l_(7399)
    aux = siblings
    _l_(7401)
    exit(aux)
elif (
    parent is not None and parent.type == syms.suite and leaf.type == token.NEWLINE
):
    _l_(7412)

    # The `# fmt: skip` is on the colon line of the if/while/def/class/...
    # statements. The ignored nodes should be previous siblings of the
    # parent suite node.
    leaf.prefix = ""
    _l_(7402)
    ignored_nodes: List[LN] = []
    _l_(7403)
    parent_sibling = parent.prev_sibling
    _l_(7404)
    while parent_sibling is not None and parent_sibling.type != syms.suite:
        _l_(7407)

        ignored_nodes.insert(0, parent_sibling)
        _l_(7405)
        parent_sibling = parent_sibling.prev_sibling
        _l_(7406)
    # Special case for `async_stmt` where the ASYNC token is on the
    # grandparent node.
    grandparent = parent.parent
    _l_(7408)
    if (
        grandparent is not None
        and grandparent.prev_sibling is not None
        and grandparent.prev_sibling.type == token.ASYNC
    ):
        _l_(7410)

        ignored_nodes.insert(0, grandparent.prev_sibling)
        _l_(7409)
    aux = iter(ignored_nodes)
    _l_(7411)
    exit(aux)
