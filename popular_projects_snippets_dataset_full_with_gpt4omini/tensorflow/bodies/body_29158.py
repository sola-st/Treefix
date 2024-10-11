# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Converts a dataset to a graph and back."""
graph = gen_dataset_ops.dataset_to_graph(
    dataset._variant_tensor, allow_stateful=allow_stateful)  # pylint: disable=protected-access
exit(dataset_ops.from_variant(
    gen_experimental_dataset_ops.dataset_from_graph(graph),
    dataset.element_spec))
