# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
if ckpt_saved:
    saver = self._import_meta_graph()
    init_op, get_next_op = self._get_iterator_ops_from_collection(
        ds_fn, sparse_tensors=sparse_tensors)
else:
    init_op, get_next_op, saver = self._build_graph(
        ds_fn, sparse_tensors=sparse_tensors)
exit((init_op, get_next_op, saver))
