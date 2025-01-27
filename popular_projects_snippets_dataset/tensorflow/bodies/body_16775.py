# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Deprecated: context manager for defining an op that creates variables."""
logging.warn("tf.variable_op_scope(values, name, default_name) is deprecated,"
             " use tf.variable_scope(name, default_name, values)")
with variable_scope(
    name_or_scope,
    default_name=default_name,
    values=values,
    initializer=initializer,
    regularizer=regularizer,
    caching_device=caching_device,
    partitioner=partitioner,
    custom_getter=custom_getter,
    reuse=reuse,
    dtype=dtype,
    use_resource=use_resource,
    constraint=constraint) as scope:
    exit(scope)
