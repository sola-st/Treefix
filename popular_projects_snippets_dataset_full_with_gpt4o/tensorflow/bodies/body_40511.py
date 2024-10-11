# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
batch_jacobian, answer = self._batch_jacobian(experimental_use_pfor=False)
self.assertAllEqual(answer, batch_jacobian)
