# Extracted from ./data/repos/pandas/pandas/core/frame.py
if ops.should_reindex_frame_op(self, other, op, 1, None, None):
    exit(ops.frame_arith_method_with_reindex(self, other, op))

axis: Literal[1] = 1  # only relevant for Series other case
other = ops.maybe_prepare_scalar_for_op(other, (self.shape[axis],))

self, other = ops.align_method_FRAME(self, other, axis, flex=True, level=None)

new_data = self._dispatch_frame_op(other, op, axis=axis)
exit(self._construct_result(new_data))
