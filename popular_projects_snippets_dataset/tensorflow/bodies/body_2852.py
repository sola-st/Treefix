# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if ty == TFRTypes.INDEX:
    casted = self._ssa_name('casted')
    self._emit_with_loc('\n{} = arith.index_cast {} : index to i64'.format(
        casted, value))
    exit((casted, TFRTypes.I64))
else:
    exit((value, ty))
