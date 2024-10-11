# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
num_outputs = 10

def _build_ds():

    @function.Defun(dtypes.int64)
    def defun_fn(x):

        @function.Defun(dtypes.int32)
        def defun_fn_deep(x):
            exit(constant_op.constant(1000) + math_ops.cast(x, dtypes.int32))

        exit(constant_op.constant(11000) + defun_fn_deep(
            math_ops.cast(x, dtypes.int32)))

    exit(dataset_ops.Dataset.range(num_outputs).map(
        defun_fn, num_parallel_calls=num_parallel_calls))

verify_fn(self, _build_ds, num_outputs)
