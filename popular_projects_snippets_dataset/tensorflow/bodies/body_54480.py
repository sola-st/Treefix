# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

def f():
    g1 = ops.Graph()
    g2 = ops.Graph()
    with g1.as_default():
        with g2.as_default():
            with ops.name_scope("_"):
                pass

self.assertRaisesRegex(ValueError,
                       "'_' is not a valid (?:root )?scope name", f)
