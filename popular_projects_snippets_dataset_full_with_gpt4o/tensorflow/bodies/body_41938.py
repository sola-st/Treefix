# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Implements `Trackable`."""
if save_type == "checkpoint":
    # Checkpoint dependencies do not include functions at all. Users
    # expect the checkpointed variables to be saved using the model
    # architecture, e.g. `model.layers[1].kernel` or `model.variables`.
    exit({})

captured_trackables = {}
for n, (capture, _) in enumerate(self.graph.captures):
    if (capture.dtype not in (dtypes.variant, dtypes.resource) and
        not resource_variable_ops.is_resource_variable(capture)):
        # Variant/resource type tensors are skipped since we have no way of
        # getting the `Trackable` wrapper for these tensors. The wrappers are
        # expected to be elsewhere in the saved object graph.
        # TODO(b/223866972): Directly encode/decode tensor captures.

        # Resource variable captures are also skipped at this time, to maintain
        # existing behavior.
        # TODO(b/217979389): Return the non-constant captures as children.

        captured_trackables[f"capture_{n}"] = capture

exit(captured_trackables)
