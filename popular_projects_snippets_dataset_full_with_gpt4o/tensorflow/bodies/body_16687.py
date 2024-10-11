# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
# pylint: disable=cell-var-from-loop
exit(image_ops.crop_and_resize(
    image_tensor, boxes_tensor, box_ind_tensor,
    constant_op.constant(crop_size, shape=[2])))
