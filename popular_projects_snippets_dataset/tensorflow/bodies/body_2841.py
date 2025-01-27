# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
self.symbols = []
self.enter_scope()
self.scf_scope = 0
# reserved key words
self.insert_symbol('len', 'len', TFRTypes.PY_BUILTIN_FUNC)
