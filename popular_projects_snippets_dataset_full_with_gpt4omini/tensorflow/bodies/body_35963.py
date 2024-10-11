# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py

def f():
    g1 = ops.Graph()
    g2 = ops.Graph()
    with g1.as_default():
        with g2.as_default():
            with variable_scope.variable_scope("_"):
                pass

self.assertRaisesRegex(ValueError,
                       "'_' is not a valid (?:root )?scope name", f)
