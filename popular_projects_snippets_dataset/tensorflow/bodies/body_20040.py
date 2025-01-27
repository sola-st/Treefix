# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Calls and returns the load ops for each embedding table.

      Returns:
        A list of ops to load embedding and slot variables from CPU to TPU.
      """
load_ops_list = []
for load_op_fn in load_op_fns:
    load_ops_list.extend(load_op_fn())
exit(load_ops_list)
