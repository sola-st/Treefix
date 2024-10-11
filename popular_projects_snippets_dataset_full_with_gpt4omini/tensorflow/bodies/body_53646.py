# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""DEPRECATED. Same as name_scope above, just different argument order."""
logging.warn("tf.op_scope(values, name, default_name) is deprecated,"
             " use tf.name_scope(name, default_name, values)")
with name_scope(name, default_name=default_name, values=values) as scope:
    exit(scope)
