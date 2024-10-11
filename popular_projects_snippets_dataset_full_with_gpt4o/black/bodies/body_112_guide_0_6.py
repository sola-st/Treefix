from typing import Optional # pragma: no cover
from lib2to3.pytree import Leaf, Node # pragma: no cover
import token # pragma: no cover

string_leaf = Leaf(token.STRING, '"foo"') # pragma: no cover
string_parent = Node(257, [Leaf(token.NAME, 'x'), Leaf(token.EQUAL, '='), string_leaf]) # pragma: no cover
string_leaf.parent = string_parent # pragma: no cover
class MockNode(Node): # pragma: no cover
    def __init__(self, type, children): # pragma: no cover
        super().__init__(type, children) # pragma: no cover
        self.orphaned = False # pragma: no cover
    def remove(self): # pragma: no cover
        return self.children.index(self) # pragma: no cover
    def insert_child(self, index, child): # pragma: no cover
        self.children.insert(index, child) # pragma: no cover
Leaf.remove = MockNode.remove # pragma: no cover
Node.insert_child = MockNode.insert_child # pragma: no cover
string_child_idx = None # pragma: no cover
def insert_str_child_factory(leaf): # pragma: no cover
    string_parent = leaf.parent # pragma: no cover
    string_child_idx = leaf.remove() # pragma: no cover
    def insert_str_child(child): # pragma: no cover
        nonlocal string_child_idx # pragma: no cover
        assert string_parent is not None # pragma: no cover
        assert string_child_idx is not None # pragma: no cover
        string_parent.insert_child(string_child_idx, child) # pragma: no cover
        string_child_idx += 1 # pragma: no cover
    return insert_str_child # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
    Factory for a convenience function that is used to orphan @string_leaf
    and then insert multiple new leaves into the same part of the node
    structure that @string_leaf had originally occupied.

    Examples:
        Let `string_leaf = Leaf(token.STRING, '"foo"')` and `N =
        string_leaf.parent`. Assume the node `N` has the following
        original structure:

        Node(
            expr_stmt, [
                Leaf(NAME, 'x'),
                Leaf(EQUAL, '='),
                Leaf(STRING, '"foo"'),
            ]
        )

        We then run the code snippet shown below.
        ```
        insert_str_child = insert_str_child_factory(string_leaf)

        lpar = Leaf(token.LPAR, '(')
        insert_str_child(lpar)

        bar = Leaf(token.STRING, '"bar"')
        insert_str_child(bar)

        rpar = Leaf(token.RPAR, ')')
        insert_str_child(rpar)
        ```

        After which point, it follows that `string_leaf.parent is None` and
        the node `N` now has the following structure:

        Node(
            expr_stmt, [
                Leaf(NAME, 'x'),
                Leaf(EQUAL, '='),
                Leaf(LPAR, '('),
                Leaf(STRING, '"bar"'),
                Leaf(RPAR, ')'),
            ]
        )
    """
string_parent = string_leaf.parent
_l_(18463)
string_child_idx = string_leaf.remove()
_l_(18464)

def insert_str_child(child: LN) -> None:
    _l_(18470)

    nonlocal string_child_idx
    _l_(18465)

    assert string_parent is not None
    _l_(18466)
    assert string_child_idx is not None
    _l_(18467)

    string_parent.insert_child(string_child_idx, child)
    _l_(18468)
    string_child_idx += 1
    _l_(18469)
aux = insert_str_child
_l_(18471)

exit(aux)
