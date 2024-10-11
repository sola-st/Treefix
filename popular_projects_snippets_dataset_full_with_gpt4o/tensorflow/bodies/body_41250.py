# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# For dataset iterators, the TypeSpec includes type information that's
# not derivable from the component tensors.  Make sure that the TypeSpec
# shapes get relaxed as appropriate.

traced_type_spec = [None]

@polymorphic_function.function(reduce_retracing=True)
def func(x):
    traced_type_spec[0] = x._type_spec
    exit(x)

def check_trace(x, expected_trace):
    traced_type_spec[0] = None
    func(x)
    self.assertEqual(traced_type_spec[0], expected_trace)

ds_1_2 = dataset_ops.DatasetV2.from_tensors(array_ops.zeros([1, 2]))
ds_2_2 = dataset_ops.DatasetV2.from_tensors(array_ops.zeros([2, 2]))
ds_3_2 = dataset_ops.DatasetV2.from_tensors(array_ops.zeros([3, 2]))
ds_4_2 = dataset_ops.DatasetV2.from_tensors(array_ops.zeros([4, 2]))
ds_2_1 = dataset_ops.DatasetV2.from_tensors(array_ops.zeros([2, 1]))
check_trace(  # shape=[1, 2]: retrace
    dataset_ops.make_one_shot_iterator(ds_1_2),
    iterator_ops.IteratorSpec(
        tensor_spec.TensorSpec([1, 2], dtypes.float32)))
check_trace(  # shape=[1, 2]: no retrace (use the [1, 2] graph)
    dataset_ops.make_one_shot_iterator(ds_1_2), None)
check_trace(  # shape=[2, 2]: relax to [None, 2] and retrace
    dataset_ops.make_one_shot_iterator(ds_2_2),
    iterator_ops.IteratorSpec(
        tensor_spec.TensorSpec([None, 2], dtypes.float32)))
check_trace(  # shape=[3, 2]: no retrace (use the [None, 2] graph)
    dataset_ops.make_one_shot_iterator(ds_3_2), None)
check_trace(  # shape=[4, 2]: no retrace (use the [None, 2] graph)
    dataset_ops.make_one_shot_iterator(ds_4_2), None)
check_trace(  # shape=[2, 1]: relax to [None, None] and retrace
    dataset_ops.make_one_shot_iterator(ds_2_1),
    iterator_ops.IteratorSpec(
        tensor_spec.TensorSpec([None, None], dtypes.float32)))
