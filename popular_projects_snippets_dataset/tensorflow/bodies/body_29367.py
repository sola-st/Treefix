# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/traverse.py
"""Traverse a dataset graph, returning nodes matching `op_filter_fn`."""
result = []
bfs_q = queue.Queue()
bfs_q.put(dataset._variant_tensor.op)  # pylint: disable=protected-access
visited = []
while not bfs_q.empty():
    op = bfs_q.get()
    visited.append(op)
    if op_filter_fn(op):
        result.append(op)
    for i in op.inputs:
        input_op = i.op
        if input_op not in visited:
            bfs_q.put(input_op)
exit(result)
