from typing import List, Optional # pragma: no cover

class Leaf: # pragma: no cover
  def __init__(self, token: str, value: str): # pragma: no cover
    self.token = token # pragma: no cover
    self.value = value # pragma: no cover
    self.parent = None # pragma: no cover
  def remove(self) -> int: # pragma: no cover
    if self.parent is not None: # pragma: no cover
      idx = self.parent.children.index(self) # pragma: no cover
      self.parent.children.remove(self) # pragma: no cover
      self.parent = None # pragma: no cover
      return idx # pragma: no cover
    return -1 # pragma: no cover
 # pragma: no cover
class Node: # pragma: no cover
  def __init__(self, type: str, children: List): # pragma: no cover
    self.type = type # pragma: no cover
    self.children = children # pragma: no cover
    for child in self.children: # pragma: no cover
      if isinstance(child, Leaf): # pragma: no cover
        child.parent = self # pragma: no cover
  def insert_child(self, idx: int, child): # pragma: no cover
    if 0 <= idx <= len(self.children): # pragma: no cover
      self.children.insert(idx, child) # pragma: no cover
      if isinstance(child, Leaf): # pragma: no cover
        child.parent = self # pragma: no cover
 # pragma: no cover
LN = Leaf # pragma: no cover
string_leaf = Leaf('STRING', '"foo"') # pragma: no cover
string_leaf.parent = Node('expr_stmt', [ # pragma: no cover
  Leaf('NAME', 'x'), # pragma: no cover
  Leaf('EQUAL', '='), # pragma: no cover
  string_leaf # pragma: no cover
]) # pragma: no cover

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
