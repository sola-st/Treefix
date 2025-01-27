# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
batch = 2
image_height = 3
image_width = 4
crop_height = 4
crop_width = 5
depth = 2
num_boxes = 2

image_shape = [batch, image_height, image_width, depth]
crop_size = [crop_height, crop_width]
crops_shape = [num_boxes, crop_height, crop_width, depth]

image = np.arange(0, batch * image_height * image_width *
                  depth).reshape(image_shape).astype(np.float32)
boxes = np.array([[0, 0, 1, 1], [.1, .2, .7, .8]], dtype=np.float32)
box_ind = np.array([0, 1], dtype=np.int32)

crops = image_ops.crop_and_resize(
    constant_op.constant(image, shape=image_shape),
    constant_op.constant(boxes, shape=[num_boxes, 4]),
    constant_op.constant(box_ind, shape=[num_boxes]),
    constant_op.constant(crop_size, shape=[2]))
with self.session():
    self.assertEqual(crops_shape, list(crops.get_shape()))
    crops = self.evaluate(crops)
    self.assertEqual(crops_shape, list(crops.shape))
