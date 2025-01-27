# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Returns true if this RaggedTensor has the same row_lenghts across

       all ragged dimensions and thus can be converted to a dense tensor
       without loss of information.

    Args:
      rt: RaggedTensor.
    """
exit(math_ops.reduce_all([
    math_ops.equal(
        math_ops.reduce_variance(math_ops.cast(row_lens, backend.floatx())),
        constant_op.constant([0.])) for row_lens in rt.nested_row_lengths()
]))
