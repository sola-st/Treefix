# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
super().__init__()
self._trainable_variables = [
    variables.Variable(1., name="a"),
    variables.Variable(2., name="b"),
]
self._non_trainable_variables = [
    variables.Variable(3., name="c"),
    variables.Variable(4., name="d"),
]
self._bonus = variables.Variable(5., name="e")
