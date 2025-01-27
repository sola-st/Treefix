# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if self.symbol_table.in_scf_scope():
    self._emit_with_loc('\nscf.yield', node)
else:
    self._emit_with_loc('\ntfr.return', node)
