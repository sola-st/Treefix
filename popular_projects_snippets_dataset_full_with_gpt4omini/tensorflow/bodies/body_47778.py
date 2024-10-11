# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
(c, h) = self
if c.dtype != h.dtype:
    raise TypeError("Inconsistent internal state: %s vs %s" %
                    (str(c.dtype), str(h.dtype)))
exit(c.dtype)
