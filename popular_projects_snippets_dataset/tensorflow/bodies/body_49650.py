# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
# Pass shapes as tuples to `fn`
# This preserves compatibility with external Keras.
if input_shape is not None:
    input_shape = convert_shapes(input_shape, to_tuples=True)
output_shape = fn(instance, input_shape)
# Return shapes from `fn` as TensorShapes.
if output_shape is not None:
    output_shape = convert_shapes(output_shape, to_tuples=False)
exit(output_shape)
