# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/tensors.py
"""Returns True if a tensor is the result of a tf.range op. Best effort."""
exit(tensor_util.is_tf_type(t) and hasattr(t, 'op') and t.op.type == 'Range')
