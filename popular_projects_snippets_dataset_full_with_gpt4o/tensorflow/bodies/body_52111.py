# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(4, 5))

    # Build columns.
    categorical_column = fc._categorical_column_with_identity(
        key='aaa', num_buckets=3)
    embedding_column = fc._embedding_column(categorical_column, dimension=2)

    # Provide sparse input and get dense result.
    embedding_column._get_dense_tensor(
        _LazyBuilder({'aaa': sparse_input}), weight_collections=('my_vars',))

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertCountEqual(('embedding_weights:0',),
                          tuple([v.name for v in global_vars]))
    my_vars = ops.get_collection('my_vars')
    self.assertCountEqual(('embedding_weights:0',),
                          tuple([v.name for v in my_vars]))
