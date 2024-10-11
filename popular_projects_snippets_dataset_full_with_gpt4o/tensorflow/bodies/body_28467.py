# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
"""Generates elements from input dataset while stopping at break points.

    Produces `num_outputs` outputs and saves the state of the iterator in the
    Saver checkpoint.

    Args:
      ds_fn: 0-argument function that returns the dataset.
      break_points: A list of integers. For each `break_point` in
        `break_points`, we produce outputs till `break_point` number of items
        have been produced and then checkpoint the state. The current graph and
        session are destroyed and a new graph and session are used to produce
        outputs till next checkpoint or till `num_outputs` elements have been
        produced. `break_point` must be <= `num_outputs`.
      num_outputs: The total number of outputs to produce from the iterator.
      ckpt_saved: Whether a checkpoint already exists.
      sparse_tensors:  Whether dataset is built from SparseTensor(s).
      verify_exhausted: Whether to verify that the iterator has been exhausted
        after producing `num_outputs` elements.
      save_checkpoint_at_end: Whether to save a checkpoint after producing all
        outputs. If False, checkpoints are saved each break point but not at the
        end. Note that checkpoints overwrite each other so there is always only
        a single checkpoint available. Defaults to True.

    Returns:
      A list of `num_outputs` items.
    """
outputs = []

if context.executing_eagerly():
    for i in range(len(break_points) + 1):
        iterator = iter(ds_fn())
        ckpt = tracking_util.Checkpoint(iterator=iterator)
        if ckpt_saved:
            ckpt_path = self._latest_ckpt()
            ckpt.restore(ckpt_path)
        start = break_points[i - 1] if i > 0 else 0
        end = break_points[i] if i < len(break_points) else num_outputs
        num_iters = end - start
        for _ in range(num_iters):
            outputs.append(self.evaluate(next(iterator)))
        if i == len(break_points) and verify_exhausted:
            with self.assertRaises(StopIteration):
                next(iterator)
        if save_checkpoint_at_end or i < len(break_points):
            ckpt_path = ckpt.save(self._ckpt_path())
            ckpt_saved = True
else:
    def get_ops():
        if ckpt_saved:
            saver = self._import_meta_graph()
            init_op, get_next_op = self._get_iterator_ops_from_collection(
                ds_fn, sparse_tensors=sparse_tensors)
        else:
            init_op, get_next_op, saver = self._build_graph(
                ds_fn, sparse_tensors=sparse_tensors)
        exit((init_op, get_next_op, saver))

    for i in range(len(break_points) + 1):
        with ops.Graph().as_default() as g:
            init_op, get_next_op, saver = get_ops()
            get_next_op = remove_variants(get_next_op)
            with self.session(graph=g) as sess:
                if ckpt_saved:
                    self._initialize(init_op, sess)
                    self._restore(saver, sess)
                else:
                    self._initialize(init_op, sess)
                start = break_points[i - 1] if i > 0 else 0
                end = break_points[i] if i < len(break_points) else num_outputs
                num_iters = end - start
                for _ in range(num_iters):
                    outputs.append(sess.run(get_next_op))
                if i == len(break_points) and verify_exhausted:
                    with self.assertRaises(errors.OutOfRangeError):
                        sess.run(get_next_op)
                if save_checkpoint_at_end or i < len(break_points):
                    self._save(sess, saver)
                    ckpt_saved = True

exit(outputs)
