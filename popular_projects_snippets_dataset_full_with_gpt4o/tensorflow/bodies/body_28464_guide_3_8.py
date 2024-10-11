import contextlib # pragma: no cover

num_outputs = 10 # pragma: no cover
break_point = None # pragma: no cover
error = RuntimeError # pragma: no cover
sparse_tensors = False # pragma: no cover
def ds_fn(): return tf.data.Dataset.range(num_outputs) # pragma: no cover
def remove_variants(tensors): return tensors # pragma: no cover
class MockSelf: # pragma: no cover
    def _ckpt_path(self): # pragma: no cover
        return '/tmp/mock_ckpt.ckpt' # pragma: no cover
    def assertRaises(self, error): # pragma: no cover
        @contextlib.contextmanager # pragma: no cover
        def context_manager(): # pragma: no cover
            try: yield # pragma: no cover
            except error: pass # pragma: no cover
            else: raise AssertionError('Expected error not raised') # pragma: no cover
        return context_manager() # pragma: no cover
    def _build_graph(self, ds_fn, sparse_tensors): # pragma: no cover
        with ops.Graph().as_default() as g: # pragma: no cover
            dataset = ds_fn() # pragma: no cover
            iterator = dataset.make_one_shot_iterator() # pragma: no cover
            init_op = tf.compat.v1.global_variables_initializer() # pragma: no cover
            get_next_op = iterator.get_next() # pragma: no cover
            saver = tf.compat.v1.train.Saver() # pragma: no cover
            return init_op, get_next_op, saver # pragma: no cover
    def session(self, graph=None): # pragma: no cover
        return tf.compat.v1.Session(graph=graph) # pragma: no cover
    def _initialize(self, init_op, sess): # pragma: no cover
        sess.run(init_op) # pragma: no cover
    def _save(self, sess, saver): # pragma: no cover
        saver.save(sess, self._ckpt_path()) # pragma: no cover
self = MockSelf() # pragma: no cover

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
