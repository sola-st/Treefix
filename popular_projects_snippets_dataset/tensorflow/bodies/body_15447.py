# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_resize_image_op_test.py
rt = ragged_tensor.RaggedTensor.from_tensor(array_ops.zeros([5, 5, 3]))
with self.assertRaisesRegex(ValueError, 'rank must be 4'):
    image_ops.resize_images_v2(rt, [10, 10])
