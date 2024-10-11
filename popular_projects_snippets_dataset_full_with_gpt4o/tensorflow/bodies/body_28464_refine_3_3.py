num_outputs = 10 # pragma: no cover
break_point = None # pragma: no cover
context = type('Mock', (object,), {'executing_eagerly': lambda: True})() # pragma: no cover
ds_fn = lambda: tf_data.Dataset.range(100) # pragma: no cover
error = ValueError # pragma: no cover
sparse_tensors = False # pragma: no cover
remove_variants = lambda x: x # pragma: no cover

import contextlib # pragma: no cover

num_outputs = 10 # pragma: no cover
break_point = None # pragma: no cover
context = type('Mock', (object,), {'executing_eagerly': staticmethod(lambda: True)}) # pragma: no cover
ds_fn = lambda: tf.data.Dataset.range(100) # pragma: no cover
self = type('Mock', (object,), {'assertRaises': lambda self, error: contextlib.nullcontext(), '_ckpt_path': lambda self: '/tmp/ckpt', '_build_graph': lambda self, ds_fn, sparse_tensors: (None, None, None), 'session': lambda self, graph: contextlib.nullcontext(), '_initialize': lambda self, init_op, sess: None, '_save': lambda self, sess, saver: None})() # pragma: no cover
error = ValueError # pragma: no cover
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
_l_(21770)
if context.executing_eagerly():
    _l_(21786)

    iterator = iter(ds_fn())
    _l_(21771)
    ckpt = tracking_util.Checkpoint(iterator=iterator)
    _l_(21772)
    for _ in range(break_point):
        _l_(21774)

        next(iterator)
        _l_(21773)
    with self.assertRaises(error):
        _l_(21776)

        ckpt.save(self._ckpt_path())
        _l_(21775)
else:
    with ops.Graph().as_default() as g:
        _l_(21785)

        init_op, get_next_op, saver = self._build_graph(
            ds_fn, sparse_tensors=sparse_tensors)
        _l_(21777)
        get_next_op = remove_variants(get_next_op)
        _l_(21778)
        with self.session(graph=g) as sess:
            _l_(21784)

            self._initialize(init_op, sess)
            _l_(21779)
            for _ in range(break_point):
                _l_(21781)

                sess.run(get_next_op)
                _l_(21780)
            with self.assertRaises(error):
                _l_(21783)

                self._save(sess, saver)
                _l_(21782)
