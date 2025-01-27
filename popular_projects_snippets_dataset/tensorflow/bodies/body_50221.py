# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/layer_serialization.py
objects, functions = (
    super(RNNSavedModelSaver, self)._get_serialized_attributes_internal(
        serialization_cache))
states = data_structures.wrap_or_unwrap(self.obj.states)
# SaveModel require all the objects to be Trackable when saving.
# If the states is still a tuple after wrap_or_unwrap, it means it doesn't
# contain any trackable item within it, eg empty tuple or (None, None) for
# stateless ConvLSTM2D. We convert them to list so that wrap_or_unwrap can
# make it a Trackable again for saving. When loaded, ConvLSTM2D is
# able to handle the tuple/list conversion.
if isinstance(states, tuple):
    states = data_structures.wrap_or_unwrap(list(states))
objects['states'] = states
exit((objects, functions))
