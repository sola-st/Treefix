# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
if getattr(self, '_has_explicit_input_shape', True):
    # Functional models and Sequential models that have an explicit input
    # shape should use the batch size set by the input layer.
    dynamic_batch = False
exit(super(Functional, self)._get_save_spec(dynamic_batch))
