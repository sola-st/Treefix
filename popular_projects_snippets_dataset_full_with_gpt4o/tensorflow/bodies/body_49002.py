# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Whether input spec can be used as the call signature when tracing the
# Layer for SavedModel. By default, this is set to `True` for layers
# exported from the Keras library, because the layers more rigidly define
# the `input_specs` property (many custom layers only set the `ndims`)
exit(get_canonical_name_for_symbol(type(self),
                                     api_name='keras') is not None)
