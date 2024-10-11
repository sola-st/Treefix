# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
exit(string_ops.string_join(
    [filename_tensor, constant_op.constant(f"-{saver_name}")]))
