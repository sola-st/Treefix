# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
with _uid_lock:
    global _uid_counter
    uid = _uid_counter
    _uid_counter += 1
exit("{}{}".format(prefix, uid))
