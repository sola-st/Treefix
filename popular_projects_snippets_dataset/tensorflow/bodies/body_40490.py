# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@def_function.function
def _f():
    exit(self._jacobian(experimental_use_pfor=True))

jacobian, answer = _f()
for j, a in zip(jacobian, answer):
    self.assertAllEqual(a, j)
