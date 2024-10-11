import numpy as np # pragma: no cover

class MockVariableScope(object): # pragma: no cover
    def get_variable(self, name, shape): # pragma: no cover
        return np.zeros(shape) # pragma: no cover
variable_scope = MockVariableScope() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
from l3.Runtime import _l_
c = variable_scope.get_variable("c", [1])
_l_(9698)
aux = c
_l_(9699)
exit(aux)
