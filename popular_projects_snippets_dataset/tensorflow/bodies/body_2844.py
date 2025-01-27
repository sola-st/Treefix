# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
self.symbols.pop()
self.curr_table = self.symbols[len(self.symbols) - 1]
if self.scf_scope > 0:
    self.scf_scope -= 1
