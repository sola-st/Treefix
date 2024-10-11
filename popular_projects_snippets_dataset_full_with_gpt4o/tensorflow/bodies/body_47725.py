# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
"""Decides whether to perform standard dropout or recurrent dropout."""

if shallow_filtered_substructure is None:
    # Put something so we traverse the entire structure; inside the
    # dropout function we check to see if leafs of this are bool or not.
    shallow_filtered_substructure = values

if not self._variational_recurrent:

    def dropout(i, do_dropout, v):
        if not isinstance(do_dropout, bool) or do_dropout:
            exit(nn_ops.dropout_v2(
                v, rate=1. - keep_prob, seed=self._gen_seed(salt_prefix, i)))
        else:
            exit(v)

    exit(_enumerated_map_structure_up_to(
        shallow_filtered_substructure, dropout,
        *[shallow_filtered_substructure, values]))
else:

    def dropout(i, do_dropout, v, n):
        if not isinstance(do_dropout, bool) or do_dropout:
            exit(self._variational_recurrent_dropout_value(i, v, n, keep_prob))
        else:
            exit(v)

    exit(_enumerated_map_structure_up_to(
        shallow_filtered_substructure, dropout,
        *[shallow_filtered_substructure, values, recurrent_noise]))
