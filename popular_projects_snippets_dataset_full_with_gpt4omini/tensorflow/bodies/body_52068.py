# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._categorical_column_with_identity(key='aaa', num_buckets=30)
data = example_pb2.Example(features=feature_pb2.Features(
    feature={
        'aaa':
            feature_pb2.Feature(int64_list=feature_pb2.Int64List(
                value=[11, 21]))
    }))
features = parsing_ops.parse_example(
    serialized=[data.SerializeToString()],
    features=fc.make_parse_example_spec([a]))
self.assertIn('aaa', features)
_assert_sparse_tensor_value(
    self,
    sparse_tensor.SparseTensorValue(
        indices=[[0, 0], [0, 1]],
        values=np.array([11, 21], dtype=np.int64),
        dense_shape=[1, 2]), self.evaluate(features['aaa']))
