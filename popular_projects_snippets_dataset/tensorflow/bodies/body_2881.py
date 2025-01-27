# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
values = self.visit(node.value)
if self.symbol_table.in_scf_scope():
    self.emit('\nscf.yield ')
else:
    self.emit('\ntfr.return ')
if not values:
    exit()

if isinstance(values, list):
    vals, tys = zip(*values)
else:
    vals = values[0]
    tys = values[1]

if isinstance(tys, list) or isinstance(tys, tuple):
    tys = [str(t) for t in tys]
    self._emit_with_loc('{} : {}'.format(', '.join(vals), ', '.join(tys)),
                        node)
elif tys != TFRTypes.NONE:
    # TODO(fengliuai): scf region yield uses this branch. Fix it.
    self._emit_with_loc('{} : {}'.format(vals, tys), node)
