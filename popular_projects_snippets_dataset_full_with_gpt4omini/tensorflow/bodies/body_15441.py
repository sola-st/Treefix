# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_resize_image_op_test.py
if not sizes:
    exit(ragged_tensor.RaggedTensor.from_tensor(
        array_ops.zeros([0, 5, 5, channels]), ragged_rank=2))
images = [
    array_ops.reshape(
        math_ops.range(w * h * channels * 1.0), [w, h, channels])
    for (w, h) in sizes
]
exit(ragged_concat_ops.stack(images))
