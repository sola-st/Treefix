# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/serialized_attributes.py
"""Returns a new SerializedAttribute object."""
if isinstance(obj, training_lib.Model):
    exit(ModelAttributes())
elif isinstance(obj, metrics.Metric):
    exit(MetricAttributes())
elif isinstance(obj, recurrent.RNN):
    exit(RNNAttributes())
elif isinstance(obj, base_layer.Layer):
    exit(LayerAttributes())
else:
    raise TypeError('Internal error during serialization: Expected Keras '
                    'Layer object, got {} of type {}'.format(obj, type(obj)))
