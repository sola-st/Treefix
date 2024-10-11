from typing import Tuple, List # pragma: no cover
from lib2to3.pgen2.token import NAME, EQUAL, STRING, LPAR, RPAR # pragma: no cover
from lib2to3.pytree import Leaf, Node # pragma: no cover

class MockNode(Node): # pragma: no cover
    def __init__(self, type: int, children: List[Leaf]): # pragma: no cover
        pass
    def insert_child(self, index: int, child: Leaf) -> None: # pragma: no cover
        self.children.insert(index, child) # pragma: no cover
        string_child_idx = index # pragma: no cover
    def remove_child(self, child: Leaf) -> None: # pragma: no cover
        self.children.remove(child) # pragma: no cover
        string_leaf.parent = None # pragma: no cover
 # pragma: no cover
string_leaf = Leaf(STRING, '"foo"') # pragma: no cover
string_parent = MockNode(None, [Leaf(NAME, 'x'), Leaf(EQUAL, '='), string_leaf]) # pragma: no cover
string_leaf.parent = string_parent # pragma: no cover
LN = Leaf # pragma: no cover
string_child_idx = string_leaf.remove = lambda: string_parent.children.index(string_leaf) # pragma: no cover

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
