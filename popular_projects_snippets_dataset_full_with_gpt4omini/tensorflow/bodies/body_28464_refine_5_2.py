error = TypeError # pragma: no cover
sparse_tensors = False # pragma: no cover
remove_variants = lambda x: x # pragma: no cover

num_outputs = 10 # pragma: no cover
break_point = num_outputs // 2 # pragma: no cover
context = type('MockContext', (), {'executing_eagerly': lambda: True})() # pragma: no cover
ds_fn = lambda: Dataset.range(num_outputs) # pragma: no cover
self = type('MockSelf', (), {'assertRaises': staticmethod(lambda exc: (yield)), '_ckpt_path': lambda: 'mock_ckpt_path', '_build_graph': lambda ds_fn, sparse_tensors: (tf.constant(0), tf.constant(1), None), 'session': lambda graph: type('MockSession', (), {'__enter__': lambda s: s, '__exit__': lambda s, exc_type, exc_value, traceback: None, 'run': lambda x: None})()})() # pragma: no cover
error = RuntimeError('Expected error') # pragma: no cover
sparse_tensors = False # pragma: no cover
remove_variants = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
from l3.Runtime import _l_
"""Attempts to save a non-saveable iterator.

    Args:
      ds_fn: 0-argument function that returns a Dataset.
      num_outputs: Total number of outputs expected from this Dataset.
      error: Declared error when trying to save iterator.
      break_point: Break point. Optional. Defaults to num_outputs/2.
      sparse_tensors: Whether dataset is built from SparseTensor(s).

    Raises:
      AssertionError if any test fails.
    """
break_point = num_outputs // 2 if not break_point else break_point
_l_(9426)
if context.executing_eagerly():
    _l_(9442)

    iterator = iter(ds_fn())
    _l_(9427)
    ckpt = tracking_util.Checkpoint(iterator=iterator)
    _l_(9428)
    for _ in range(break_point):
        _l_(9430)

        next(iterator)
        _l_(9429)
    with self.assertRaises(error):
        _l_(9432)

        ckpt.save(self._ckpt_path())
        _l_(9431)
else:
    with ops.Graph().as_default() as g:
        _l_(9441)

        init_op, get_next_op, saver = self._build_graph(
            ds_fn, sparse_tensors=sparse_tensors)
        _l_(9433)
        get_next_op = remove_variants(get_next_op)
        _l_(9434)
        with self.session(graph=g) as sess:
            _l_(9440)

            self._initialize(init_op, sess)
            _l_(9435)
            for _ in range(break_point):
                _l_(9437)

                sess.run(get_next_op)
                _l_(9436)
            with self.assertRaises(error):
                _l_(9439)

                self._save(sess, saver)
                _l_(9438)
