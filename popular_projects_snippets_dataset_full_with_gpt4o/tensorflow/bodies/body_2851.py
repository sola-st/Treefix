# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
# This is packing a list of tensors, then the axis is 0.
axis = self._ssa_name('zero')
self._emit_with_loc('\n{} = arith.constant 0 : i64'.format(axis))
casted = self._ssa_name('pack')
self.emit('\n{} = tfr.call @tf__pack({}, {})'.format(casted, value, axis))
self._emit_with_loc(' : (!tfr.tensor_list, i64) -> !tfr.tensor')
# load the op def of tf.Pack
self._op_defs.lookup('Pack')
exit((casted, TFRTypes.TENSOR))
