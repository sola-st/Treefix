# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
if mixed_precision_global_state.is_mixed_precision_graph_rewrite_enabled():
    raise ValueError(
        'The global dtype policy cannot be set to "{policy.name}", because the '
        'mixed precision graph rewrite has already been enabled.\n'
        'At most, one of the following can be called:\n\n'
        '  1. tf.compat.v1.train.enable_mixed_precision_graph_rewrite() '
        '(You called this first)\n'
        '  2. tf.keras.mixed_precision.experimental.set_global_policy() with a '
        'mixed precision policy (You called this second)\n\n'
        'You called both functions, which is an error, because both functions '
        'enable you to use mixed precision. If in doubt which function to use, '
        'use the second, as it supports Eager execution and is more '
        'customizable.'.format(policy=policy))
