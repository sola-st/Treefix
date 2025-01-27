# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
super(TFRGen, self).__init__(ctx)
self.ctx = ctx
self.symbol_table = SymbolTable()
self._op_defs = op_defs
