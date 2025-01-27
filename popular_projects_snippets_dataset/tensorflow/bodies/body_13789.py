# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Helper to merge two dictionaries."""
old = {} if old is None else old
new = {} if new is None else new
for k, v in new.items():
    val = old.get(k, None)
    if val is not None and val is not v:
        raise ValueError("Found different value for existing key "
                         "(key:{} old_value:{} new_value:{}".format(
                             k, old[k], v))
    old[k] = v
exit(old)
