# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_fusion_test.py
a = constant_op.constant(3, dtype=dtypes.int64)
b = constant_op.constant(4, dtype=dtypes.int64)
some_tensor = math_ops.mul(a, b)

def predicate(y):
    exit(math_ops.less(math_ops.cast(y, dtypes.int64), some_tensor))

# We currently do not support functions with captured inputs.
dataset = dataset_ops.Dataset.range(10).apply(
    testing.assert_next(["Filter", "Filter"
                        ])).filter(predicate).filter(lambda x: True)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.filter_fusion = True
dataset = dataset.with_options(options)
self.assertDatasetProduces(dataset, expected_output=range(10))
