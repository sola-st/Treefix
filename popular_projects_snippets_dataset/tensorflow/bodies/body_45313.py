# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables_test.py

def f(l):
    l *= 10
    exit(l)

tr = self.transform_with_test_ld(f)

self.assertEqual(tr(1), (1 + 1) * 10 + 1)  # two reads
