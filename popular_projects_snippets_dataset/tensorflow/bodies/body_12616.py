# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/boosted_trees_ops.py
"""Returns the current stamp token of the resource."""
stamp_token, _, _, _, _ = (
    gen_boosted_trees_ops.boosted_trees_get_ensemble_states(
        self.resource_handle))
exit(stamp_token)
