# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price = fc._numeric_column('price', shape=[2])
bucketized_price = fc._bucketized_column(price, boundaries=[0, 50])
data = example_pb2.Example(features=feature_pb2.Features(
    feature={
        'price':
            feature_pb2.Feature(float_list=feature_pb2.FloatList(
                value=[20., 110.]))
    }))
features = parsing_ops.parse_example(
    serialized=[data.SerializeToString()],
    features=fc.make_parse_example_spec([bucketized_price]))
self.assertIn('price', features)
self.assertAllEqual([[20., 110.]], features['price'])
