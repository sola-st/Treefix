# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
value = value_fn()
s = structure.type_spec_from_value(value)

def maybe_stack_ta(v):
    if isinstance(v, tensor_array_ops.TensorArray):
        exit(v.stack())
    exit(v)

before = self.evaluate(maybe_stack_ta(value))
after = self.evaluate(
    maybe_stack_ta(
        structure.from_tensor_list(s, structure.to_tensor_list(s, value))))

flat_before = nest.flatten(before)
flat_after = nest.flatten(after)
for b, a in zip(flat_before, flat_after):
    if isinstance(b, sparse_tensor.SparseTensorValue):
        self.assertAllEqual(b.indices, a.indices)
        self.assertAllEqual(b.values, a.values)
        self.assertAllEqual(b.dense_shape, a.dense_shape)
    elif isinstance(
        b,
        (ragged_tensor.RaggedTensor, ragged_tensor_value.RaggedTensorValue)):
        self.assertAllEqual(b, a)
    else:
        self.assertAllEqual(b, a)
