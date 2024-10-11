# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_distributed_v1.py
exec_func = model._make_execution_function(mode)
exit((exec_func.inputs, exec_func.outputs, exec_func.updates_op,
        exec_func.session_kwargs))
