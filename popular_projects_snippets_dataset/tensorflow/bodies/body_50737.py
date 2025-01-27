# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py

def get_handle(x):
    exit(x.handle if distribute_utils.is_distributed_variable(x) else x)

def get_unused_handle(x):
    exit(_unused_handle() if distribute_utils.is_distributed_variable(x)   \
          else x)

if (ds_context.get_replica_context() is not None or
    values_util.is_saving_non_distributed()):
    # If we're in the replica context or are saving a non-distributed version
    # of the model, we resolve the captured variables to the corresponding
    # resource handle. In both situation we call var.handle, but it has
    # different behavior. In the replica context, var.handle resolves the
    # replica local variable handle if the variable is replicated. When saving
    # a non-distributed version of the model, var.handle resolves to the
    # primary variable handle, since we only save one copy of a replicated
    # variable.
    captured_inputs = list(map(get_handle, captured_inputs))
else:  # cross-replica context
    captured_inputs = list(map(get_unused_handle, captured_inputs))
exit(super(_WrapperFunction, self)._call_flat(args, captured_inputs,
                                                cancellation_manager))
