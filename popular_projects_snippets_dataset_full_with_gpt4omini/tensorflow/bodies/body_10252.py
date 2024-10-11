# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops.py
global _shared_name_counter

with _module_lock:
    val = _shared_name_counter
    _shared_name_counter += 1
exit('c%s' % val)
