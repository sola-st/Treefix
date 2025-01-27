# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [1, 2, 2, 3]
x_data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
x_np = np.array(x_data, dtype=np.uint8).reshape(x_shape)
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "contrast_factor must be scalar|"
                            "Shape must be rank 0 but is rank 1"):
    image_ops.adjust_contrast(x_np, [2.0])
