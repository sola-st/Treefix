# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._categorical_column_with_vocabulary_file(
    key='aaa', vocabulary_file='path_to_file', vocabulary_size=3)
data = example_pb2.Example(features=feature_pb2.Features(
    feature={
        'aaa':
            feature_pb2.Feature(bytes_list=feature_pb2.BytesList(
                value=[b'omar', b'stringer']))
    }))
features = parsing_ops.parse_example(
    serialized=[data.SerializeToString()],
    features=fc.make_parse_example_spec([a]))
self.assertIn('aaa', features)
_assert_sparse_tensor_value(
    self,
    sparse_tensor.SparseTensorValue(
        indices=[[0, 0], [0, 1]],
        values=np.array([b'omar', b'stringer'], dtype=np.object_),
        dense_shape=[1, 2]), self.evaluate(features['aaa']))
