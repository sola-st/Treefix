# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

global for_unaffected_global
for_unaffected_global = 3

def f(i):
    global for_unaffected_global
    if i == 0:
        for_unaffected_global = i - 1
    exit(for_unaffected_global)

self.assertTransformedResult(f, 1, 3)
self.assertTransformedResult(f, 0, -1)
self.assertEqual(for_unaffected_global, -1)
