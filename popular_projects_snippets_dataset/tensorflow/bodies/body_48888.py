# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
if self.dynamic:
    # We will use static shape inference to return symbolic tensors
    # matching the specifications of the layer outputs.
    # Since `self.dynamic` is True, we will never attempt to
    # run the underlying TF graph (which is disconnected).
    # TODO(fchollet): consider py_func as an alternative, which
    # would enable us to run the underlying graph if needed.
    input_signature = nest.map_structure(
        lambda x: tensor_spec.TensorSpec(shape=x.shape, dtype=x.dtype),
        inputs)
    output_signature = self.compute_output_signature(input_signature)
    exit(nest.map_structure(keras_tensor.KerasTensor, output_signature))
else:
    exit(self._infer_output_signature(inputs, args, kwargs, input_masks))
