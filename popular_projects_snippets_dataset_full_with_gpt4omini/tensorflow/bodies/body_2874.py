# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
self.emit('\n')
ret_str, ret_ssa_values = self._get_mlir_ssa_values(
    'for_stmt', [TFRTypes.TENSOR] * len(loop_carried))
if ret_ssa_values:
    self.emit(ret_str + ' = ')

# Before enter the loop, we use the original ssa values as the initial
# values to the loop iteration arguments. We also create new ssa values as
# the returns of the scf for statements. The symbol table needs to be
# updated to these new ssa values before it enters the scope of the loop.
out_types = []
init_values = []
for symbol, ssa_value in zip(loop_carried, ret_ssa_values):
    init, ty = self.symbol_table.lookup(symbol)
    self.symbol_table.insert_symbol(symbol, ssa_value, ty)
    out_types.append(str(ty))
    init_values.append((init, ty))

# Create a new scope in case the local variables are leaked.
self.symbol_table.enter_scope(scf_scope=True)

# Create the iteration variable with index type
assert len(body_def.args.args) == 1
it_name = body_def.args.args[0].id
it = self._ssa_name(it_name)
self.symbol_table.insert_symbol(it_name, it, TFRTypes.INDEX)

self.emit('scf.for {} = {} to {} step {} '.format(it, range_[0], range_[1],
                                                  range_[2]))
if loop_carried:
    iter_args = []
    for symbol, init in zip(loop_carried, init_values):
        # create new ssa values for the loop carried variables
        it_arg = self._ssa_name('it_arg')
        self.symbol_table.insert_symbol(symbol, it_arg, init[1])
        iter_args.append('{} = {}'.format(it_arg, init[0]))
    self.emit('iter_args({}) '.format(', '.join(iter_args)))
    self.emit('-> ({}) {{'.format(', '.join(out_types)))
else:
    self.emit(' {')
self.visit_block(body_def.body)
self.visit_block(get_state.body)
self.symbol_table.exit_scope()
self._emit_with_loc('\n}', node)
exit(list(zip(ret_ssa_values, out_types)))
