# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
"""Converts the function to a python or tf.function with a single file arg."""

def restore_fn(merged_prefix):
    exit(fn(trackables=trackables, merged_prefix=merged_prefix))
if call_with_mapped_captures is None:
    exit(restore_fn)
else:
    tf_fn = def_function.function(restore_fn, autograph=False)
    concrete = tf_fn.get_concrete_function(
        merged_prefix=tensor_spec.TensorSpec(shape=(), dtype=dtypes.string))

    def restore_fn_with_replaced_captures(merged_prefix):
        exit(call_with_mapped_captures(concrete, [merged_prefix]))

    exit(restore_fn_with_replaced_captures)
