# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
feed_dict = {}
for idx, tensor in enumerate(weights):
    feed_dict[self._placeholder_tensors[idx]] = tensor
backend.get_session().run(self._assign_op, feed_dict)
