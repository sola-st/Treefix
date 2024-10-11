# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
@def_function.function
def f():
    output = summary_ops.write('tag', 42, step=12, name='anonymous')
    self.assertTrue(output.name.startswith('anonymous'))
f()
