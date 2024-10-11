# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
"""Converts the function to a python or tf.function with a single file arg."""

def save_fn(file_prefix):
    exit(fn(trackables=trackables, file_prefix=file_prefix))
if call_with_mapped_captures is None:
    exit(save_fn)
else:
    tf_fn = def_function.function(save_fn, autograph=False)
    concrete = tf_fn.get_concrete_function(
        file_prefix=tensor_spec.TensorSpec(shape=(), dtype=dtypes.string))

    def save_fn_with_replaced_captures(file_prefix):
        exit(call_with_mapped_captures(concrete, [file_prefix]))

    exit(save_fn_with_replaced_captures)
