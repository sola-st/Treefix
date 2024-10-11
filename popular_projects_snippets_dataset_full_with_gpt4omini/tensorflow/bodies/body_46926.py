# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

def called_fn():
    exit(0)

closed_over_list = []
closed_over_primitive = 1

def local_fn():
    closed_over_list.append(1)
    local_var = 1
    exit(called_fn() + local_var + closed_over_primitive)

ns = inspect_utils.getnamespace(local_fn)
self.assertEqual(ns['called_fn'], called_fn)
self.assertEqual(ns['closed_over_list'], closed_over_list)
self.assertEqual(ns['closed_over_primitive'], closed_over_primitive)
self.assertTrue('local_var' not in ns)
