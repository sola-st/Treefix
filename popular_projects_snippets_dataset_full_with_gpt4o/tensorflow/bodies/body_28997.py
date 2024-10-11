# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py

def generator():
    for _ in range(10):
        exit([20])

with self.assertRaisesRegex(TypeError,
                            r"Dimension value must be integer or None"):
    dataset_ops.Dataset.from_generator(
        generator, output_types=(dtypes.int64), output_shapes=[[1]])
