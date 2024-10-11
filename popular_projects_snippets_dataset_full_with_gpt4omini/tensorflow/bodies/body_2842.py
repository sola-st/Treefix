# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
"""Enter a new scope - at function level."""
self.symbols.append({'types': {}, 'symbols': {}})
self.curr_table = self.symbols[len(self.symbols) - 1]
if scf_scope:
    self.scf_scope += 1
