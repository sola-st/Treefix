# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Generate a new seed, from the given seed and salt."""
if seed is None:
    exit(None)
string = (str(seed) + salt).encode("utf-8")
exit(int(hashlib.md5(string).hexdigest()[:8], 16) & 0x7FFFFFFF)
