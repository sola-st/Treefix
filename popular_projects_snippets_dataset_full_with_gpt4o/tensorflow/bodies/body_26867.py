# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_fusion_test.py
a = constant_op.constant(3, dtype=dtypes.int64)
b = constant_op.constant(4, dtype=dtypes.int64)
some_tensor = math_ops.mul(a, b)

# We currently do not support functions with captured inputs.
dataset = dataset_ops.Dataset.range(1).apply(
    testing.assert_next(["Map", "Map"
                        ])).map(lambda x: some_tensor).map(lambda x: x)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.map_fusion = True
dataset = dataset.with_options(options)
self.assertDatasetProduces(dataset, expected_output=[some_tensor])
