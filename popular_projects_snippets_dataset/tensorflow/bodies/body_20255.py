# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py

# Inputs.
input_sparse_tensor = sparse_tensor.SparseTensorValue(
    indices=((0, 0), (1, 0), (1, 1), (1, 4)),
    values=(2, 0, 1, 3),
    dense_shape=(2, 5))
input_features = {'inp': input_sparse_tensor}

# Build columns.
categorical_column_input = fc_lib.categorical_column_with_identity(
    key='inp', num_buckets=3)

# Training on TPU with cpu embedding lookups is not supported.
if shared:
    embedding_column = tpu_fc.shared_embedding_columns_v2(
        [categorical_column_input],
        dimension=2,
        embedding_lookup_device='cpu',
        tensor_core_shape=[None, 3])
else:
    embedding_column = tpu_fc.embedding_column_v2(
        categorical_column_input,
        dimension=2,
        embedding_lookup_device='cpu',
        tensor_core_shape=[None, 3])
dense_features = df_lib.DenseFeatures(embedding_column)
with self.assertRaisesRegex(
    ValueError,
    r'.*embedding_lookup_device=\"cpu\" during training is not'):
    dense_features(input_features)

# Inference on with TPU Embedding Hardware is not supported.
if shared:
    embedding_column = tpu_fc.shared_embedding_columns_v2(
        [categorical_column_input],
        dimension=2,
        embedding_lookup_device='tpu_embedding_core',
        tensor_core_shape=[None, 3])
else:
    embedding_column = tpu_fc.embedding_column_v2(
        categorical_column_input,
        dimension=2,
        embedding_lookup_device='tpu_embedding_core',
        tensor_core_shape=[None, 3])
context = tpu._TPUInferenceContext('tpu_inference')
context.Enter()
dense_features = df_lib.DenseFeatures(embedding_column)
with self.assertRaisesRegex(
    ValueError,
    r'Using embedding_lookup_device=tpu_embedding_core during inference is '
):
    dense_features(input_features)
context.Exit()
