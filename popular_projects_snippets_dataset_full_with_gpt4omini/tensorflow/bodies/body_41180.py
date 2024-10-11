# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/saved_model_exported_concrete.py
"""Raises AssertionError due to being unable to export a function."""
msg = ("Tried to export a function which references an 'untracked' resource. "
       "TensorFlow objects (e.g. tf.Variable) captured by functions must be "
       "'tracked' by assigning them to an attribute of a tracked object or "
       "assigned to an attribute of the main object directly. See the "
       "information below:"
       f"\n\tFunction name = {function_name}")

if node_path is not None:
    msg += f"\n\tPath to Function = {node_path}"

msg += f"\n\tCaptured Tensor = {capture}"
msg += f"\n\t{_get_trackable_parent_error_string(capture)}"

if internal_capture is not None:
    msg += f"\n\tInternal Tensor = {internal_capture}"
raise AssertionError(msg)
