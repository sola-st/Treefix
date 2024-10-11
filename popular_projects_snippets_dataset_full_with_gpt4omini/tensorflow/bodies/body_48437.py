# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
if not self.built:
    try:
        # If this is a Numpy array or tensor, we can get shape from .shape.
        # If not, an attribute error will be thrown.
        data_shape = data.shape
        data_shape_nones = tuple([None] * len(data.shape))
    except AttributeError:
        # The input has an unknown number of dimensions.
        data_shape = None
        data_shape_nones = None

    # TODO (b/159261555): move this to base layer build.
    batch_input_shape = getattr(self, '_batch_input_shape', None)
    if batch_input_shape is None:
        # Set the number of dimensions.
        self._batch_input_shape = data_shape_nones
    self.build(data_shape)
    self.built = True
