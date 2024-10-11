# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
some_op = lambda x: x
some_op = dispatch.add_type_based_api_dispatcher(some_op)
with self.assertRaisesRegex(
    ValueError, ".* already has a type-based API dispatcher."):
    some_op = dispatch.add_type_based_api_dispatcher(some_op)
