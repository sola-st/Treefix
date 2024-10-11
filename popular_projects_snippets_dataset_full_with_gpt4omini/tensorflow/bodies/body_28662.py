# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
self._testDatasetSpec(
    {
        "a": constant_op.constant(37.0),
        "b": (constant_op.constant(["Foo"]), constant_op.constant("Bar"))
    }, {
        "a":
            tensor_spec.TensorSpec([], dtypes.float32),
        "b": (
            tensor_spec.TensorSpec([1], dtypes.string),
            tensor_spec.TensorSpec([], dtypes.string),
        )
    })
