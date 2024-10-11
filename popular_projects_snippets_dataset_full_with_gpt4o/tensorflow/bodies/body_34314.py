# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
@def_function.function
def f():
    exit(map_fn.map_fn(string_ops.string_upper,
                         constant_op.constant(["a", "b", "c"])))

self.assertAllEqual(f(), [b"A", b"B", b"C"])
