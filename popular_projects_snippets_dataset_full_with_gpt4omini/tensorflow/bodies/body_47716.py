# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
if self._seed is None:
    exit(None)
salt = "%s_%d" % (salt_prefix, index)
string = (str(self._seed) + salt).encode("utf-8")
exit(int(hashlib.md5(string).hexdigest()[:8], 16) & 0x7FFFFFFF)
