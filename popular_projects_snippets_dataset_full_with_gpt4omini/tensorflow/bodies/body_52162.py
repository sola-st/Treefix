# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
column = fc._weighted_categorical_column(
    categorical_column=fc._categorical_column_with_identity(
        key='ids', num_buckets=3),
    weight_feature_key='values')
with ops.Graph().as_default():
    predictions = fc.linear_model(
        {
            'ids':
                sparse_tensor.SparseTensorValue(
                    indices=((0, 0), (1, 0), (1, 1)),
                    values=(0, 2, 1),
                    dense_shape=(2, 2)),
            'values': ((.5,), (1.,))
        }, (column,),
        sparse_combiner='mean')
    # Disabling the constant folding optimizer here since it changes the
    # error message differently on CPU and GPU.
    config = config_pb2.ConfigProto()
    config.graph_options.rewrite_options.constant_folding = (
        rewriter_config_pb2.RewriterConfig.OFF)
    with _initialized_session(config):
        with self.assertRaisesRegex(errors.OpError, 'Incompatible shapes'):
            self.evaluate(predictions)
