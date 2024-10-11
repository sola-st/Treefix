class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
def cached_session(self): return tf.compat.v1.Session() # pragma: no cover
self.cached_session = cached_session # pragma: no cover
self.assertEqual = lambda x, y: None # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.cached_session = lambda: None # pragma: no cover
self.assertEqual = lambda a, b: print(f'Assert: {a} == {b}') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v1_12.py
from l3.Runtime import _l_
sp_input = tf.SparseTensor(
    indices=tf.constant([[0, 1]], dtype=tf.int64),
    values=tf.constant([2], dtype=tf.int64),
    dense_shape=[1, 2])
_l_(6774)

with self.cached_session():
    _l_(6777)

    serialized_sp = tf.serialize_many_sparse(
        sp_input, 'serialize_name', tf.string)
    _l_(6775)
    self.assertEqual((1, 3), serialized_sp.shape)
    _l_(6776)
