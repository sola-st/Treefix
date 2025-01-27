# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
self.emit('\n')
ret_str, ret_ssa_values = self._get_mlir_ssa_values(
    'if_stmt', [TFRTypes.TENSOR] * len(out_symbols))
if ret_ssa_values:
    self.emit(ret_str + ' = ')

out_types = []
for symbol, ssa_value in zip(out_symbols, ret_ssa_values):
    out_types.append(str(TFRTypes.TENSOR))

self.emit('scf.if {} -> ({}) {{'.format(cond, ', '.join(out_types)))
# Create a new scope in case the local variables are leaked.
self.symbol_table.enter_scope(scf_scope=True)
self.visit_block(body_def.body)
self.visit_block(get_state.body)
self.symbol_table.exit_scope()

self.emit('\n} else {')

# Create a new scope in case the local variables are leaked.
self.symbol_table.enter_scope(scf_scope=True)
self.visit_block(orelse_def.body)
self.visit_block(get_state.body)
self.symbol_table.exit_scope()

# add ssa values to the symbol table
for symbol, ssa_value in zip(out_symbols, ret_ssa_values):
    self.symbol_table.insert_symbol(symbol, ssa_value, TFRTypes.TENSOR)

self._emit_with_loc('\n}', node)
exit(list(zip(ret_ssa_values, out_types)))
