# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
if host_id >= len(x.variables):
    # In the edge case where we have more hosts than variables, due to using
    # a small number of rows, we load zeros for the later hosts. We copy
    # the shape of the first host's variables, which we assume is defined
    # because TableConfig guarantees at least one row.
    exit(array_ops.zeros_like(x.variables[0]))
exit(x.variables[host_id])
