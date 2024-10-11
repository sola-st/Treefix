# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/layer_utils.py
if not getattr(layer, '_keras_api_names', None):
    exit(False)

# Subclasses of `Layer` that are not exported inherit the export name
# of the base layer class.
exit((layer._keras_api_names != ('keras.layers.Layer',) and
        layer._keras_api_names_v1 != ('keras.layers.Layer',)))
