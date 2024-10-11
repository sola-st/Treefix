# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/variables_test.py
undefined_symbol = variables.Undefined('name')
undefined_symbol2 = variables.Undefined('name')

self.assertEqual(undefined_symbol.symbol_name, 'name')
self.assertEqual(undefined_symbol2.symbol_name, 'name')
self.assertNotEqual(undefined_symbol, undefined_symbol2)
