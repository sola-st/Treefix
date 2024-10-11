# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
input_list = nest.flatten(inputs)
if any(isinstance(x, ragged_tensor.RaggedTensor) for x in input_list):
    raise ValueError('Layer %s does not support RaggedTensors as input. '
                     'Inputs received: %s. You can try converting your '
                     'input to an uniform tensor.' % (layer_name, inputs))
