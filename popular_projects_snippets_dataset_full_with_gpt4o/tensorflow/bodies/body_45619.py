# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives_test.py
a = 1
while True:
    a = 2
    directives.set_loop_options(parallel_iterations=10, back_prop=a)  # pylint: disable=unexpected-keyword-arg
