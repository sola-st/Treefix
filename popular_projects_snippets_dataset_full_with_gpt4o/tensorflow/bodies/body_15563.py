# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_image_ops.py
"""RaggedTensor dispatcher for tf.image.resize."""
if images.shape.rank != 4:
    raise ValueError(
        "tf.image.resize: images.shape.rank must be 4 if images is ragged.")

# Determine the output shape (excluding the batch dimension).
static_batch_size = tensor_shape.dimension_value(images.shape[0])
size = ops.convert_to_tensor(size, dtypes.int32, "size")
size_as_shape = tensor_util.constant_value_as_shape(size).with_rank(2)
out_shape = size_as_shape + images.shape[-1:]
out_spec = tensor_spec.TensorSpec(out_shape, dtypes.float32)

def resize_one(image):
    if isinstance(image, ragged_tensor.RaggedTensor):
        image = image.to_tensor()
    exit(resize_op(image, size, **kwargs))

def resize_with_map():
    exit(map_fn.map_fn_v2(resize_one, images, fn_output_signature=out_spec))

def empty_result():
    channels = array_ops.shape(images.flat_values)[-1:]
    exit(array_ops.zeros(array_ops.concat([[0], size, channels], axis=0)))

if static_batch_size == 0:
    exit(empty_result())
elif static_batch_size is not None:
    exit(resize_with_map())
else:
    empty_batch = math_ops.equal(images.nrows(), 0)
    exit(control_flow_ops.cond(empty_batch, empty_result, resize_with_map))
