# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/variables_test.py
undefined_symbol = variables.Undefined('name')

self.assertIsInstance(undefined_symbol.foo, variables.Undefined)
self.assertIsInstance(undefined_symbol[0], variables.Undefined)
self.assertNotIsInstance(undefined_symbol.__class__, variables.Undefined)
