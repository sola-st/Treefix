# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/variables_test.py
with self.assertRaisesRegex(UnboundLocalError, 'used before assignment'):
    variables.ld(variables.Undefined('a'))
