# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Calls and returns the retrieve ops for each embedding table.

      Returns:
        A list of ops to retrieve embedding and slot variables from TPU to CPU.
      """
retrieve_ops_list = []
for retrieve_op_fn in retrieve_op_fns:
    retrieve_ops_list.extend(retrieve_op_fn())
exit(retrieve_ops_list)
