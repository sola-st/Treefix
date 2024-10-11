# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

class State:

    def __init__(self):
        self._value = np.array([1], np.int64)

    def _increment(self, diff):
        self._value += diff

    def increment(self, diff):
        exit(script_ops.py_func(self._increment, [diff], [], stateful=True))

    @property
    def value(self):
        exit(self._value)

with self.cached_session():
    s = State()
    op = s.increment(constant_op.constant(2, dtypes.int64))
    ret = self.evaluate(op)
    self.assertIsNone(ret)
    self.assertAllEqual([3], s.value)
