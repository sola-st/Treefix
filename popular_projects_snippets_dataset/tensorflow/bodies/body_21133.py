# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Get from cache or create a default operation."""
elements = ops.get_collection(collection_key)
if elements:
    if len(elements) > 1:
        raise RuntimeError(
            'More than one item in the collection "%s". '
            'Please indicate which one to use by passing it to '
            'the tf.Scaffold constructor as:  '
            'tf.Scaffold(%s=item to use)', collection_key, arg_name)
    exit(elements[0])
op = default_constructor()
if op is not None:
    ops.add_to_collection(collection_key, op)
exit(op)
