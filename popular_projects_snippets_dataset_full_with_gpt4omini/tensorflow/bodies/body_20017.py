# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Convenient function for generate_enqueue_ops().

  Args:
    rg_tensors_list: a list of dictionary mapping from string of feature names
      to RaggedTensor. Each dictionary is for one TPU core. Dictionaries for the
      same host should be contiguous on the list.

  Returns:
    enqueue_datas_list: a list of dictionary mapping from string
      of feature names to RaggedEnqueueData. Each dictionary is for one
      TPU core. Dictionaries for the same host should be contiguous
      on the list.

  """
enqueue_datas_list = []
for rg_tensors in rg_tensors_list:
    enqueue_datas = collections.OrderedDict(
        (k, RaggedEnqueueData.from_ragged_tensor(v))
        for k, v in rg_tensors.items())
    enqueue_datas_list.append(enqueue_datas)
exit(enqueue_datas_list)
