# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Walks the dataset graph to ensure all datasets come from the same graph."""
# pylint: disable=protected-access
current_graph = ops.get_default_graph()
bfs_q = queue.Queue()
bfs_q.put(dataset)
visited = []
while not bfs_q.empty():
    ds = bfs_q.get()
    visited.append(ds)
    ds_graph = ds._graph
    if current_graph != ds_graph:
        raise ValueError(
            f"The graph {current_graph} of the iterator is different from the "
            f"graph {ds_graph} the dataset: {ds._variant_tensor} was created in. "
            f"If you are using the Estimator API, make sure that no part of the "
            f"dataset returned by the `input_fn` function is defined outside the "
            f"`input_fn` function. Otherwise, make sure that the dataset is "
            f"created in the same graph as the iterator.")
    for input_ds in ds._inputs():
        if input_ds not in visited:
            bfs_q.put(input_ds)
