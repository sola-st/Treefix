# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    categorical_column_a = fc._categorical_column_with_identity(
        key='aaa', num_buckets=3)
    categorical_column_b = fc._categorical_column_with_identity(
        key='bbb', num_buckets=3)
    embedding_dimension = 2
    embedding_column_b, embedding_column_a = fc_new.shared_embedding_columns(
        [categorical_column_b, categorical_column_a],
        dimension=embedding_dimension)
    all_cols = [embedding_column_a, embedding_column_b]

    features = {
        'aaa':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=(0, 1, 0),
                dense_shape=(2, 2)),
        'bbb':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=(1, 2, 1),
                dense_shape=(2, 2)),
    }
    fc.input_layer(features, all_cols)
    # Make sure that only 1 variable gets created in this case.
    self.assertEqual(1, len(
        ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)))

with ops.Graph().as_default():
    features1 = {
        'aaa':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=(0, 1, 0),
                dense_shape=(2, 2)),
        'bbb':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=(1, 2, 1),
                dense_shape=(2, 2)),
    }

    fc.input_layer(features1, all_cols)
    # Make sure that only 1 variable gets created in this case.
    self.assertEqual(1, len(
        ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)))
    self.assertCountEqual(
        ['input_layer/aaa_bbb_shared_embedding/embedding_weights:0'],
        [v.name for v in ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)])
