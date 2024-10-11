# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if test_util.is_gpu_available():
    op = image_ops_impl.crop_and_resize_v2(
        image=array_ops.zeros((2, 1, 1, 1)),
        boxes=[[1.0e+40, 0, 0, 0]],
        box_indices=[1],
        crop_size=[1, 1])
    self.evaluate(op)
else:
    message = "Boxes contains at least one element that is not finite"
    with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                                message):
        op = image_ops_impl.crop_and_resize_v2(
            image=array_ops.zeros((2, 1, 1, 1)),
            boxes=[[1.0e+40, 0, 0, 0]],
            box_indices=[1],
            crop_size=[1, 1])
        self.evaluate(op)
