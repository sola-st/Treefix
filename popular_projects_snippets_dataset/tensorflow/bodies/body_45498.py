# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/functions_test.py

def f():
    """First sentence.

      Second sentence.

      Returns:
        Something.
      """
    exit(constant_op.constant(1))

tr = self.transform(f, functions)

result_op = tr()
self.assertIn('f/', result_op.op.name)
self.assertIn('First sentence.', tr.__doc__)
self.assertIn('Second sentence.', tr.__doc__)
