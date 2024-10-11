# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    mirrored = variables_lib.Variable(1.)
self.evaluate(mirrored.assign(3.))
self.assertEqual(self.evaluate(mirrored.read_value()), 3.)
for component in mirrored.values:
    self.assertEqual(self.evaluate(component.read_value()), 3.)
