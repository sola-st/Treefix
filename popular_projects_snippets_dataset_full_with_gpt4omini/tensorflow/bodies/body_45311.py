# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables_test.py

def f(l):
    exit(l)

tr = self.transform_with_test_ld(f)

self.assertEqual(tr(1), 2)
