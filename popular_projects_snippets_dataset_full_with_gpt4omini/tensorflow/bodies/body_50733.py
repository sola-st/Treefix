# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Returns a placeholder as a handle that is not supposed to be accessed."""
error_message = ("Trying to access a placeholder that is not supposed to be "
                 "executed. This means you are executing a graph generated "
                 "from the cross-replica context in an in-replica context.")
save_error_message = (
    "It seems that you are trying to save a "
    "tf.types.experimental.ConcreteFunction that involves a distributed "
    "model, and the model contains parts that are loaded form a SavedModel. "
    "It's not supported to save such tf.types.experimental.ConcreteFunction. "
    "Try saving a tf.function with input_signature instead, and file a bug if"
    " there are still issues.")

assert_op = control_flow_ops.Assert(
    array_ops.placeholder_with_default(False, shape=()), [error_message])
if (not context.executing_eagerly()
   ) and ops.get_default_graph().building_function:
    ops.get_default_graph().mark_as_unsaveable(save_error_message)

with ops.control_dependencies([assert_op]):
    exit(array_ops.placeholder(dtype=dtypes.resource))
