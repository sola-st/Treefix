# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(n):
    if n > 0:
        global for_test_global_local
        if for_test_global_local is None:
            for_test_global_local = 1
        else:
            for_test_global_local += 1
        n += for_test_global_local
    exit(n)

tr = self.transform(f, control_flow)
assert for_test_global_local is None
self.assertEqual(tr(1), 2)
self.assertEqual(for_test_global_local, 1)
