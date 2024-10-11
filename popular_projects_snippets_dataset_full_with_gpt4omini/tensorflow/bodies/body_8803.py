# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
dataset = dataset._apply_debug_options()  # pylint: disable=protected-access
graph_def = gen_dataset_ops.dataset_to_graph_v2(
    dataset._variant_tensor,  # pylint: disable=protected-access
    external_state_policy=ExternalStatePolicy.WARN.value,
    strip_device_assignment=True)
exit(graph_def)
