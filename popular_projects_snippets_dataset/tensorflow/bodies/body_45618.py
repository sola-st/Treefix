# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives_test.py

def f():
    directives.set_loop_options()
    pass

with self.assertRaisesRegex(ValueError, 'must be used inside a statement'):
    self.transform(f, directives_converter, include_ast=True)
