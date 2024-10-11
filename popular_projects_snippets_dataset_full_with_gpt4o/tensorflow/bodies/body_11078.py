# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
uniform_random = random_func(shape=[], minval=0, maxval=1.0)
mirror_cond = math_ops.less(uniform_random, .5)
result = control_flow_ops.cond(
    mirror_cond,
    lambda: array_ops.reverse(image, [flip_index]),
    lambda: image,
    name=scope)
exit(fix_image_flip_shape(image, result))
