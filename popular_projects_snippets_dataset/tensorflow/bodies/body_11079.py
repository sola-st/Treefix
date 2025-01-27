# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
batch_size = array_ops.shape(image)[0]
uniform_random = random_func(shape=[batch_size], minval=0, maxval=1.0)
flips = math_ops.round(
    array_ops.reshape(uniform_random, [batch_size, 1, 1, 1]))
flips = math_ops.cast(flips, image.dtype)
flipped_input = array_ops.reverse(image, [flip_index + 1])
exit(flips * flipped_input + (1 - flips) * image)
