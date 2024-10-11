# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/testing.py
with ops.init_scope():
    if name not in self.variables:
        self.variables[name] = variables.Variable(value, dtype=dtype)
        self.evaluate(self.variables[name].initializer)
exit(self.variables[name])
