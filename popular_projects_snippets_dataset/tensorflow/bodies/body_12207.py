# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2_indexed_slices_rewriter.py
assert old_output.type == "Identity"
concat_op = old_output.inputs[0].op
assert concat_op.type == "ConcatV2"
# Don't include axis arg
old_concat_args = concat_op.inputs[:-1]
# We assume that the original gradient input was the first argument to the
# concat op.
# TODO(skyewm): do this in a more robust way.
exit(array_ops.concat([new_input] + old_concat_args[1:], 0))
