# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
dispatch_apis = dispatch.apis_with_type_based_dispatch()
self.assertIn(math_ops.add, dispatch_apis)
self.assertIn(array_ops.concat, dispatch_apis)
