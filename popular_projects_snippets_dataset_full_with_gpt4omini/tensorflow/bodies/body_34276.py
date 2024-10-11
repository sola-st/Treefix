# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.cached_session() as sess:
    # Use placeholders instead of constant values for shapes to prevent TF's
    # shape inference from catching this early.
    l1_element_shape = array_ops.placeholder(dtype=dtypes.int32)
    l2_element_shape = array_ops.placeholder(dtype=dtypes.int32)
    l1 = list_ops.tensor_list_reserve(
        element_shape=l1_element_shape,
        element_dtype=dtypes.float32,
        num_elements=3)
    l2 = list_ops.tensor_list_reserve(
        element_shape=l2_element_shape,
        element_dtype=dtypes.float32,
        num_elements=3)
    l = math_ops.add_n([l1, l2])
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        "Trying to add two lists of tensors with incompatible element shapes"
    ):
        sess.run(
            list_ops.tensor_list_stack(l, element_dtype=dtypes.float32), {
                l1_element_shape: [],
                l2_element_shape: [2]
            })
