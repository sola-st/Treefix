# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
column = fc._categorical_column_with_vocabulary_file(
    key='aaa',
    vocabulary_file=self._wire_vocabulary_file_name,
    vocabulary_size=self._wire_vocabulary_size)
inputs = sparse_tensor.SparseTensor(
    values=['omar', 'stringer', 'marlo'],
    indices=[[0, 0], [1, 0], [1, 1]],
    dense_shape=[2, 2])
column._get_sparse_tensors(
    _LazyBuilder({
        'aaa': inputs
    }), weight_collections=('my_weights',))

self.assertCountEqual([],
                      ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES))
self.assertCountEqual([], ops.get_collection('my_weights'))
