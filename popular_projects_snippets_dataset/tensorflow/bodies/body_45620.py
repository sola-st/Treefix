# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives_test.py

def f():
    a = 1
    while True:
        a = 2
        directives.set_loop_options(parallel_iterations=10, back_prop=a)  # pylint: disable=unexpected-keyword-arg

with self.assertRaisesRegex(ValueError, 'must be the first statement'):
    self.transform(f, directives_converter, include_ast=True)
