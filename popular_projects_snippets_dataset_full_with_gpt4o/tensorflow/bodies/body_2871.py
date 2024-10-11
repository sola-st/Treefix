# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
"""Create MLIR convention SSA values."""
out_ssa_values = []
if not out_types:
    exit(('', out_ssa_values))

out_name = self._ssa_name(name_prefix)
if len(out_types) == 1:
    out_name_suffix = ''
    out_ssa_values.append(out_name)
else:
    # For multiple returns, MLIR uses '%s:i' when they are defined and
    # '%s#i' when they are used.
    out_name_suffix = ':{}'.format(len(out_types))
    for idx, _ in enumerate(out_types):
        out_ssa_values.append('{}#{}'.format(out_name, idx))

exit(('{}{}'.format(out_name, out_name_suffix), out_ssa_values))
