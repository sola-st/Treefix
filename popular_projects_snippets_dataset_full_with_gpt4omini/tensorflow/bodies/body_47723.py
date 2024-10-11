# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
if not isinstance(do_dropout, bool) or do_dropout:
    exit(nn_ops.dropout_v2(
        v, rate=1. - keep_prob, seed=self._gen_seed(salt_prefix, i)))
else:
    exit(v)
