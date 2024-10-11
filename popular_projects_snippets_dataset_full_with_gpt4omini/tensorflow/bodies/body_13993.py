# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
for src_t, tgt_t in zip(src_tensors, tgt_tensors):
    handle_data_util.copy_handle_data(src_t, tgt_t)
