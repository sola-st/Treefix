# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
state_manager = fc._StateManagerImpl(
    dense_features.DenseFeatures(column), trainable=True)
column.create_state(state_manager)
dense_tensor, lengths = column.get_sequence_dense_tensor(
    fc.FeatureTransformationCache(features), state_manager)
exit((dense_tensor, lengths, state_manager))
