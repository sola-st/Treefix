# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
jacobian, answer = self._jacobian(experimental_use_pfor=False)
for j, a in zip(jacobian, answer):
    self.assertAllEqual(a, j)
