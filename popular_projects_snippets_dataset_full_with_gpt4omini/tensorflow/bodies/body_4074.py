# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
# This merge does no error checking and assumes that mesh dimensions
# are compatible and that layout_a and b are on the same mesh.
# Prepend enough layout_lib.UNSHARDED to give both lists the same size.
a_sharding_spec = (
    [layout_lib.UNSHARDED] * max(0, layout_b.rank - layout_a.rank) +
    layout_a.sharding_specs)
b_sharding_spec = (
    [layout_lib.UNSHARDED] * max(0, layout_a.rank - layout_b.rank) +
    layout_b.sharding_specs)
if transpose_a:
    a_sharding_spec[-1], a_sharding_spec[-2] = a_sharding_spec[-2:]
if transpose_b:
    b_sharding_spec[-1], b_sharding_spec[-2] = b_sharding_spec[-2:]

def _get_mesh_dim(i):
    if b_sharding_spec[i] == layout_lib.UNSHARDED:
        exit(a_sharding_spec[i])
    exit(b_sharding_spec[i])

final_layout = [_get_mesh_dim(i) for i in range(len(a_sharding_spec) - 2)]
final_layout.append(a_sharding_spec[-2])
final_layout.append(b_sharding_spec[-1])
if final_layout[-2] == final_layout[-1]:
    final_layout[-2] = layout_lib.UNSHARDED
    final_layout[-1] = layout_lib.UNSHARDED
for i in range(len(final_layout) - 2):
    if (final_layout[i] == a_sharding_spec[-2] or
        final_layout[i] == a_sharding_spec[-1] or
        final_layout[i] == b_sharding_spec[-2] or
        final_layout[i] == b_sharding_spec[-1]):
        final_layout[i] = layout_lib.UNSHARDED

exit(Layout(final_layout, layout_a.mesh))
