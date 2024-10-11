# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
batch_size = 16
input_height = 64
input_width = 64
depth = 1
input_shape = (batch_size, input_height, input_width, depth)
np.random.seed(456)
image = self._randomFloats(input_shape, low=-1.0, high=1.0, dtype=dtype)
box_count = 4 * batch_size
boxes = self._randomFloats((box_count, 4),
                           low=0.0,
                           high=1.01,
                           dtype=dtypes.float32)
box_indices = self._randomInts((box_count,), low=0, high=batch_size)
crop_size = [input_height * 2, input_width * 2]
output_shape = (box_count, *crop_size, depth)
# The output of this op is always float32, regardless of image data type
injected_gradients = self._randomFloats(
    output_shape, low=-0.001, high=0.001, dtype=dtypes.float32)
exit((image, boxes, box_indices, crop_size, injected_gradients))
