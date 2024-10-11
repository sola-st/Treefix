# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/metric_serialization.py
exit((dict(variables=data_structures.wrap_or_unwrap(self.obj.variables)),
        dict()))  # TODO(b/135550038): save functions to enable saving
