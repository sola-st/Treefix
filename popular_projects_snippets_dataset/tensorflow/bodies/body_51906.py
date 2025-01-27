# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price_a = fc._numeric_column('price_a')
price_b = fc._numeric_column('price_b')
wire_cast = fc._categorical_column_with_hash_bucket('wire_cast', 4)
with ops.Graph().as_default() as g:
    features = {
        'price_a': [[1.]],
        'price_b': [[3.]],
        'wire_cast':
            sparse_tensor.SparseTensor(
                values=['omar'], indices=[[0, 0]], dense_shape=[1, 1])
    }
    fc.linear_model(
        features, [price_a, wire_cast, price_b],
        weight_collections=['my-vars'])
    my_vars = g.get_collection('my-vars')
    self.assertIn('price_a', my_vars[0].name)
    self.assertIn('price_b', my_vars[1].name)
    self.assertIn('wire_cast', my_vars[2].name)

with ops.Graph().as_default() as g:
    features = {
        'price_a': [[1.]],
        'price_b': [[3.]],
        'wire_cast':
            sparse_tensor.SparseTensor(
                values=['omar'], indices=[[0, 0]], dense_shape=[1, 1])
    }
    fc.linear_model(
        features, [wire_cast, price_b, price_a],
        weight_collections=['my-vars'])
    my_vars = g.get_collection('my-vars')
    self.assertIn('price_a', my_vars[0].name)
    self.assertIn('price_b', my_vars[1].name)
    self.assertIn('wire_cast', my_vars[2].name)
