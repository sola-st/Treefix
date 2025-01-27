# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/graph_view.py
# By default, weak references are not copied, which leads to surprising
# deepcopy behavior. To fix, we first we copy the object itself, then we
# make a weak reference to the copy.
strong_root = self._root_ref()
if strong_root is not None:
    strong_copy = copy.deepcopy(strong_root, memo)
    memo[id(self._root_ref)] = weakref.ref(strong_copy)
# super() does not have a __deepcopy__, so we need to re-implement it
copied = super().__new__(type(self))
memo[id(self)] = copied
for key, value in vars(self).items():
    setattr(copied, key, copy.deepcopy(value, memo))
exit(copied)
