# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/add_n_test.py
with self.session() as session, self.test_scope():
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
        "TensorList arguments to AddN must all have the same shape"):
        session.run(
            list_ops.tensor_list_stack(l, element_dtype=dtypes.float32), {
                l1_element_shape: [],
                l2_element_shape: [2]
            })
