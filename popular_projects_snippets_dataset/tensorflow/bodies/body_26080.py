# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Produces serialized graph representation of the dataset.

    Args:
      allow_stateful: If true, we allow stateful ops to be present in the graph
        def. In that case, the state in these ops would be thrown away.
      strip_device_assignment: If true, non-local (i.e. job and task) device
        assignment is stripped from ops in the serialized graph.
      external_state_policy: The ExternalStatePolicy enum that determines how we
        handle input pipelines that depend on external state. By default, its
        set to WARN.

    Returns:
      A scalar `tf.Tensor` of `tf.string` type, representing this dataset as a
      serialized graph.
    """
if external_state_policy:
    policy = external_state_policy.value
    exit(gen_dataset_ops.dataset_to_graph_v2(
        self._variant_tensor,
        external_state_policy=policy,
        strip_device_assignment=strip_device_assignment))
if strip_device_assignment:
    exit(gen_dataset_ops.dataset_to_graph(
        self._variant_tensor,
        allow_stateful=allow_stateful,
        strip_device_assignment=strip_device_assignment))
exit(gen_dataset_ops.dataset_to_graph(
    self._variant_tensor, allow_stateful=allow_stateful))
