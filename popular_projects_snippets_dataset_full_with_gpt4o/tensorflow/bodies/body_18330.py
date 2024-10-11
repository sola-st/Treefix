# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Stacks unstacked inputs at `stack_indices`.

    Args:
      stack_indices: indices of inputs at which stacking is done. If None,
        stacking is done at all indices.
      tile_variants: If True, affected indices which have a variant dtype will
        be tiled after this operation to match the expected shape of a
        vectorized tensor. Variants generally need to be un-tiled when they are
        inputs to operations and tiled when returned.
    """
if stack_indices is None:
    stack_indices = range(len(self._inputs))
length = self.pfor.loop_len_vector
for i in stack_indices:
    inp = self._inputs[i]
    is_variant = inp.t.dtype == dtypes.variant
    if not inp.is_stacked:
        self._inputs[i] = _stack(inp.t, length)
        if tile_variants and is_variant:
            self._inputs[i] = wrap(
                _tile_variant_with_length(self._inputs[i].t, length), True)
    elif not tile_variants and is_variant:
        self._inputs[i] = wrap(_untile_variant(self._inputs[i].t), True)
