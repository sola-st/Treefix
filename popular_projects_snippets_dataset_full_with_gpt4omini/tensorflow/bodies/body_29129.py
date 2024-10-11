# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_spec_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(
    np.arange(10).astype(np.int32)).batch(5)

@def_function.function(input_signature=[
    dataset_ops.DatasetSpec(
        tensor_spec.TensorSpec(
            shape=(None,), dtype=dtypes.int32, name=None),
        tensor_shape.TensorShape([]))
])
def fn(_):
    pass

fn(dataset)
