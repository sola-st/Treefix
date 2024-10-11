def OuterBody(i, j): return i + 1, j + 1.0 # pragma: no cover

class MockOps:  # Mock ops class to simulate TensorFlow ops # pragma: no cover
    @staticmethod # pragma: no cover
    def device(name): # pragma: no cover
        class ContextMock: # pragma: no cover
            def __enter__(self): pass # pragma: no cover
            def __exit__(self, *args): pass # pragma: no cover
        return ContextMock() # pragma: no cover
ops = MockOps() # pragma: no cover
def OuterBody(i, j): return i + 1, j + 1.0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
from l3.Runtime import _l_
with ops.device("/cpu:0"):
    _l_(7819)

    r = control_flow_ops.while_loop(
        lambda *_: True,
        OuterBody, (0, 1.0),
        maximum_iterations=5,
        name="outer")
    _l_(7817)
    aux = array_ops.identity(r[1])
    _l_(7818)
    exit(aux)
