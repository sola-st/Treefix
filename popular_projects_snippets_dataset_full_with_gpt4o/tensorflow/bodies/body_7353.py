# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy.py
if callable(initial_value):
    init_var = ops.convert_to_tensor(initial_value())
else:
    init_var = ops.convert_to_tensor(initial_value)
rank = init_var.shape.rank
exit(d_api.copy_to_mesh(
    init_var, layout.Layout.replicated(self._mesh, rank)))
