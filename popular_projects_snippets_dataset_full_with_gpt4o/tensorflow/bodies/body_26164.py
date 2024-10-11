# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Factory function for a dataset."""
# NOTE(mrry): `Defun` does not capture the graph-level seed from the
# enclosing graph, so if a graph-level seed is present we set the local
# graph seed based on a combination of the graph- and op-level seeds.
if graph_level_seed is not None:
    assert op_level_seed is not None
    core_random_seed.set_random_seed(
        (graph_level_seed + 87654321 * op_level_seed) % (2 ** 63 - 1))

dataset = self._apply_debug_options()
exit(dataset._variant_tensor)  # pylint: disable=protected-access
