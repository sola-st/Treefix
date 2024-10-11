from typing import List # pragma: no cover
import token # pragma: no cover

syms = type('syms', (object,), {'suite': 'suite'}) # pragma: no cover
class MockNode: # pragma: no cover
    def __init__(self, prefix='', node_type=None, prev_sibling=None, parent=None): # pragma: no cover
        self.prefix = prefix # pragma: no cover
        self.type = node_type # pragma: no cover
        self.prev_sibling = prev_sibling # pragma: no cover
        self.parent = parent # pragma: no cover
parent_prev_sibling = MockNode(node_type='not_suite') # pragma: no cover
grandparent_prev_sibling = MockNode(node_type=token.ASYNC) # pragma: no cover
grandparent = MockNode(prev_sibling=grandparent_prev_sibling) # pragma: no cover
parent = MockNode(node_type=syms.suite, prev_sibling=parent_prev_sibling, parent=grandparent) # pragma: no cover
leaf = MockNode(prefix='# fmt: skip', node_type=token.NEWLINE, parent=parent) # pragma: no cover
comment = type('MockComment', (object,), {'value': '# fmt: skip'})() # pragma: no cover
preview = None # pragma: no cover
def list_comments(prefix, is_endmarker=False, preview=None): # pragma: no cover
    return [type('MockComment', (object,), {'value': prefix.strip()})()] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Generate all leaves that should be ignored by the `# fmt: skip` from `leaf`."""
prev_sibling = leaf.prev_sibling
_l_(19330)
parent = leaf.parent
_l_(19331)
# Need to properly format the leaf prefix to compare it to comment.value,
# which is also formatted
comments = list_comments(leaf.prefix, is_endmarker=False, preview=preview)
_l_(19332)
if not comments or comment.value != comments[0].value:
    _l_(19334)

    exit()
    _l_(19333)
if prev_sibling is not None:
    _l_(19352)

    leaf.prefix = ""
    _l_(19335)
    siblings = [prev_sibling]
    _l_(19336)
    while "\n" not in prev_sibling.prefix and prev_sibling.prev_sibling is not None:
        _l_(19339)

        prev_sibling = prev_sibling.prev_sibling
        _l_(19337)
        siblings.insert(0, prev_sibling)
        _l_(19338)
    aux = siblings
    _l_(19340)
    exit(aux)
elif (
    parent is not None and parent.type == syms.suite and leaf.type == token.NEWLINE
):
    _l_(19351)

    # The `# fmt: skip` is on the colon line of the if/while/def/class/...
    # statements. The ignored nodes should be previous siblings of the
    # parent suite node.
    leaf.prefix = ""
    _l_(19341)
    ignored_nodes: List[LN] = []
    _l_(19342)
    parent_sibling = parent.prev_sibling
    _l_(19343)
    while parent_sibling is not None and parent_sibling.type != syms.suite:
        _l_(19346)

        ignored_nodes.insert(0, parent_sibling)
        _l_(19344)
        parent_sibling = parent_sibling.prev_sibling
        _l_(19345)
    # Special case for `async_stmt` where the ASYNC token is on the
    # grandparent node.
    grandparent = parent.parent
    _l_(19347)
    if (
        grandparent is not None
        and grandparent.prev_sibling is not None
        and grandparent.prev_sibling.type == token.ASYNC
    ):
        _l_(19349)

        ignored_nodes.insert(0, grandparent.prev_sibling)
        _l_(19348)
    aux = iter(ignored_nodes)
    _l_(19350)
    exit(aux)
