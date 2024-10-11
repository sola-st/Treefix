# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
f = model._make_execution_function(mode)
exit((f.inputs, f.outputs, f.updates_op, f.session_kwargs))
