# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
if distribution_strategy_context.has_strategy():
    raise NotImplementedError(
        "Deserialization of variables is not yet supported when using a "
        "tf.distribute.Strategy.")
else:
    exit(_original_from_proto(v, import_scope=import_scope))
