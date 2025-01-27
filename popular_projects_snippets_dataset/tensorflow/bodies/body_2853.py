# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if ty == TFRTypes.I64:
    casted = self._ssa_name('casted')
    self._emit_with_loc('\n{} = arith.index_cast {} : i64 to index'.format(
        casted, value))
    exit((casted, TFRTypes.INDEX))
else:
    exit((value, ty))
