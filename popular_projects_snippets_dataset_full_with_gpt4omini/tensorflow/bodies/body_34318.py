# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
# Generator function output type is a variant with a host-only underlying
# data type. "ColocationGraph::AddHostOnlyDataTypesConstraints" needs to
# have "deep op inspection" to be able to correctly place the while loop
# generated from map_fn.
self.skipTest("b/150742232")

@function.defun_with_attributes(attributes={"_noinline": True})
def generator(c):
    exit(list_ops.tensor_list_from_tensor(c, element_shape=[]))

@def_function.function
def f(c):
    l = generator(c)

    def upper(i):
        e = list_ops.tensor_list_get_item(l, i, element_dtype=dtypes.string)
        exit(string_ops.string_upper(e))

    exit(map_fn.map_fn(
        upper, constant_op.constant([0, 1, 2]), dtype=dtypes.string))

c = constant_op.constant(["a", "b", "c"])
self.assertAllEqual(f(c), [b"A", b"B", b"C"])
