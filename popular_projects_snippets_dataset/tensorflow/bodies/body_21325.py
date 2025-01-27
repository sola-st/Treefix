# Extracted from ./data/repos/tensorflow/tensorflow/python/training/gradient_descent.py
learning_rate = self._call_if_callable(self._learning_rate)
self._learning_rate_tensor = ops.convert_to_tensor(
    learning_rate, name="learning_rate")
