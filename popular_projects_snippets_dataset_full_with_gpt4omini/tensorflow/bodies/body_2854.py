# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
value, ty = self._index_to_I64(value, ty)
cst_tensor = self._ssa_name('cst')
self.emit('\n{} = "tfr.constant_tensor"({})'.format(cst_tensor, value))
self._emit_with_loc(' : ({}) -> !tfr.tensor'.format(ty), node)
exit((cst_tensor, TFRTypes.TENSOR))
