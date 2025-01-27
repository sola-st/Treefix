# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
values = self.visit(node.value)
if isinstance(node.targets[0], ast.Tuple):
    targets = [elt.id for elt in node.targets[0].elts]
elif isinstance(node.targets[0], ast.Name):
    targets = [node.targets[0].id]
else:
    raise NotImplementedError('Assignment target type not recognized.')

if isinstance(values, list):
    if isinstance(node.value, ast.Call):
        expected = tuple(t for n, t in values)
        if len(values) == 1:
            expected = expected[0]
    elif isinstance(node.value, ast.Tuple):
        expected = tuple(t for n, t in values)
    else:
        raise ValueError('unknown assignment target node', node.value)
    ty = self._get_inferred_type(node.value, expected)

    if len(targets) == len(values):
        # TODO(mdan): This should already be a tuple.
        ty_ = (ty,) if len(values) == 1 else ty
        for key, value, t in zip(targets, values, ty_):
            ssa_value, _ = value
            self.symbol_table.insert_symbol(key, ssa_value, t)
    elif len(values) == 1:
        name, tys = values[0]
        if ty == TFRTypes.TENSOR_LIST:
            # assign single tensor_list to multiple variables
            for idx, key in enumerate(targets):
                idx_name = self._ssa_name('idx')
                self._emit_with_loc(
                    '\n{} = arith.constant {} : index'.format(idx_name, idx), node)
                elt_name = self._ssa_name('elt')
                self.emit('\n{} = tfr.get_element {}[{}]'.format(
                    elt_name, name, idx_name))
                self._emit_with_loc(' : (!tfr.tensor_list, index) -> !tfr.tensor',
                                    node)
                self.symbol_table.insert_symbol(key, elt_name, TFRTypes.TENSOR)
        else:
            # assign single value to multiple targets. This single value is
            # usually a function return. The return type should be in the tuple of
            # the value.
            for idx, key in enumerate(targets):
                ssa_name = '{}#{}'.format(name, idx)
                ssa_type = tys[idx]
                self.symbol_table.insert_symbol(key, ssa_name, ssa_type)
    elif len(targets) == 1:
        ssa_names = [n for n, _ in values]
        self.symbol_table.insert_symbol(targets[0], ssa_names, ty)
    exit()

ty = self._get_inferred_type(node.value, values[1])
self.symbol_table.insert_symbol(targets[0], values[0], ty)
