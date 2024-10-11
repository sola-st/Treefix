# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
# BoundedTensorSpec has its own decoder.
exit((isinstance(pyobj, tensor_spec.TensorSpec) and
        not isinstance(pyobj, tensor_spec.BoundedTensorSpec)))
