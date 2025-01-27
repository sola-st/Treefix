# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
# First do a regular deepcopy of `self`.
cls = self.__class__
result = cls.__new__(cls)
memo[id(self)] = result
for k, v in self.__dict__.items():
    setattr(result, k, copy.deepcopy(v, memo))
# One little fix-up: we want `result._extended` to reference `result`
# instead of `self`.
result._extended._container_strategy_weakref = weakref.ref(result)  # pylint: disable=protected-access
exit(result)
