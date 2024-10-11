# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_keras_util.py
raise ValueError(
    'Model {} cannot be saved because the input shapes have not been '
    'set. Usually, input shapes are automatically determined from calling'
    ' `.fit()` or `.predict()`. To manually set the shapes, call '
    '`model.build(input_shape)`.'.format(model))
