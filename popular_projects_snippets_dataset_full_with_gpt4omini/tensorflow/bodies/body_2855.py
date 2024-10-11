# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if isinstance(prefix, qual_names.QN):
    assert prefix.is_simple(), 'ANF transform should have cleaned this up'
    prefix = prefix.ssf()
exit('%' + self.ctx.namer.new_symbol(prefix, set()))
