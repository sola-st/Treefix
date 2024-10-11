# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@def_function.function
def _f():
    exit(self._batch_jacobian(experimental_use_pfor=True))

batch_jacobian, answer = _f()
self.assertAllEqual(answer, batch_jacobian)
