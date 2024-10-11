# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    a = fc._categorical_column_with_vocabulary_list(
        key='aaa', vocabulary_list=('omar', 'stringer', 'marlo'))
    b = fc._categorical_column_with_vocabulary_list(
        key='bbb', vocabulary_list=('omar', 'stringer', 'marlo'))
    a_embedded, b_embedded = fc_new.shared_embedding_columns([a, b],
                                                             dimension=2)
    data = example_pb2.Example(
        features=feature_pb2.Features(
            feature={
                'aaa':
                    feature_pb2.Feature(
                        bytes_list=feature_pb2.BytesList(
                            value=[b'omar', b'stringer'])),
                'bbb':
                    feature_pb2.Feature(
                        bytes_list=feature_pb2.BytesList(
                            value=[b'stringer', b'marlo'])),
            }))
    features = parsing_ops.parse_example(
        serialized=[data.SerializeToString()],
        features=fc.make_parse_example_spec([a_embedded, b_embedded]))
    self.assertIn('aaa', features)
    self.assertIn('bbb', features)
    with self.cached_session():
        _assert_sparse_tensor_value(
            self,
            sparse_tensor.SparseTensorValue(
                indices=[[0, 0], [0, 1]],
                values=np.array([b'omar', b'stringer'], dtype=np.object_),
                dense_shape=[1, 2]), features['aaa'].eval())
        _assert_sparse_tensor_value(
            self,
            sparse_tensor.SparseTensorValue(
                indices=[[0, 0], [0, 1]],
                values=np.array([b'stringer', b'marlo'], dtype=np.object_),
                dense_shape=[1, 2]), features['bbb'].eval())
