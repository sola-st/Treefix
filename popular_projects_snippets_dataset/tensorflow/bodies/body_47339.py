# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Instantiate a model.

    Args:
      model_layers: a list of layers to be added to the model.
      *args: Model's args
      **kwargs: Model's keyword args, at most one of input_tensor -> the input
        tensor required for ragged/sparse input.
    """

inputs = kwargs.pop('input_tensor', None)
super(_SubclassModel, self).__init__(*args, **kwargs)
# Note that clone and build doesn't support lists of layers in subclassed
# models. Adding each layer directly here.
for i, layer in enumerate(model_layers):
    setattr(self, self._layer_name_for_i(i), layer)

self.num_layers = len(model_layers)

if inputs is not None:
    self._set_inputs(inputs)
