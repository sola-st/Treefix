# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
# Define three mutually incompatible nested values/structures, and assert
# that:
# 1. Using one structure to flatten a value with an incompatible structure
#    fails.
# 2. Using one structure to restructure a flattened value with an
#    incompatible structure fails.

value_0 = {
    "a": constant_op.constant(37.0),
    "b": constant_op.constant([1, 2, 3])
}
s_0 = structure.type_spec_from_value(value_0)
flat_s_0 = structure.to_tensor_list(s_0, value_0)

# `value_1` has compatible nested structure with `value_0`, but different
# classes.
value_1 = {
    "a":
        constant_op.constant(37.0),
    "b":
        sparse_tensor.SparseTensor(
            indices=[[0, 0]], values=[1], dense_shape=[1, 1])
}
s_1 = structure.type_spec_from_value(value_1)
flat_s_1 = structure.to_tensor_list(s_1, value_1)

# `value_2` has incompatible nested structure with `value_0` and `value_1`.
value_2 = {
    "a":
        constant_op.constant(37.0),
    "b": (sparse_tensor.SparseTensor(
        indices=[[0, 0]], values=[1], dense_shape=[1, 1]),
          sparse_tensor.SparseTensor(
              indices=[[3, 4]], values=[-1], dense_shape=[4, 5]))
}
s_2 = structure.type_spec_from_value(value_2)
flat_s_2 = structure.to_tensor_list(s_2, value_2)

with self.assertRaisesRegex(
    ValueError, r"SparseTensor.* is not convertible to a tensor with "
    r"dtype.*int32.* and shape \(3,\)"):
    structure.to_tensor_list(s_0, value_1)

with self.assertRaisesRegex(
    ValueError, "The two structures don't have the same nested structure."):
    structure.to_tensor_list(s_0, value_2)

with self.assertRaisesRegex(TypeError,
                            "neither a SparseTensor nor SparseTensorValue"):
    structure.to_tensor_list(s_1, value_0)

with self.assertRaisesRegex(
    ValueError, "The two structures don't have the same nested structure."):
    structure.to_tensor_list(s_1, value_2)

# NOTE(mrry): The repr of the dictionaries is not sorted, so the regexp
# needs to account for "a" coming before or after "b". It might be worth
# adding a deterministic repr for these error messages (among other
# improvements).
with self.assertRaisesRegex(
    ValueError, "The two structures don't have the same nested structure."):
    structure.to_tensor_list(s_2, value_0)

with self.assertRaisesRegex(
    ValueError, "The two structures don't have the same nested structure."):
    structure.to_tensor_list(s_2, value_1)

with self.assertRaisesRegex(ValueError,
                            r"Cannot create a Tensor from the tensor list"):
    structure.from_tensor_list(s_0, flat_s_1)

with self.assertRaisesRegex(ValueError, "Expected 2 tensors but got 3"):
    structure.from_tensor_list(s_0, flat_s_2)

with self.assertRaisesRegex(
    ValueError, "Cannot create a SparseTensor from the tensor list"):
    structure.from_tensor_list(s_1, flat_s_0)

with self.assertRaisesRegex(ValueError, "Expected 2 tensors but got 3"):
    structure.from_tensor_list(s_1, flat_s_2)

with self.assertRaisesRegex(ValueError, "Expected 3 tensors but got 2"):
    structure.from_tensor_list(s_2, flat_s_0)

with self.assertRaisesRegex(ValueError, "Expected 3 tensors but got 2"):
    structure.from_tensor_list(s_2, flat_s_1)
