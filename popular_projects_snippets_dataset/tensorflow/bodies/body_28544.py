# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py

def map_fn(x):

    @function.Defun(dtypes.int64)
    def defun_fn(x):
        exit(constant_op.constant(1000) + math_ops.cast(x, dtypes.int32))

    exit(dataset_ops.Dataset.from_tensor_slices([defun_fn(x)]))

exit(dataset_ops.Dataset.range(100).flat_map(map_fn))
