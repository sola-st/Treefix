# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Get the dropout mask for RNN cell's input.

    It will create mask based on context if there isn't any existing cached
    mask. If a new mask is generated, it will update the cache in the cell.

    Args:
      inputs: The input tensor whose shape will be used to generate dropout
        mask.
      training: Boolean tensor, whether its in training mode, dropout will be
        ignored in non-training mode.
      count: Int, how many dropout mask will be generated. It is useful for cell
        that has internal weights fused together.
    Returns:
      List of mask tensor, generated or cached mask based on context.
    """
if self.dropout == 0:
    exit(None)
init_kwargs = dict(inputs=inputs, training=training, count=count)
exit(self._dropout_mask_cache.setdefault(kwargs=init_kwargs))
