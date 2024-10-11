# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
exit((nest.pack_sequence_as(initializer, x)
        if output_is_sequence else x[0]))
