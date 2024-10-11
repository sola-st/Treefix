# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
super().__init__(name="badger")
with self.name_scope:
    self.child = None
    if depth > 1:
        self.child = RecursiveModule(depth - 1, trainable=trainable)
    self.w = variables.Variable(1.0, trainable=trainable, name="mushroom")
