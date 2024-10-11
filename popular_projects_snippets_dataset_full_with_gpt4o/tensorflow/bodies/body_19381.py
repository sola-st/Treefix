# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_checkpoint_test.py
strategy = self._get_strategy()

with strategy.scope():
    first_mid_level_contents = np.ones((4, 4))
    first_mid_level_optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
    initializer = init_ops_v2.Constant(first_mid_level_contents)

    table = tpu_embedding_v2_utils.TableConfig(
        vocabulary_size=4,
        dim=4,
        initializer=initializer,
        combiner='sum',
        name='table')
    feature_config = (tpu_embedding_v2_utils.FeatureConfig(
        table=table, name='feature'),)

    first_mid_level = tpu_embedding_v1.TPUEmbeddingV0(
        feature_config, first_mid_level_optimizer)

    first_mid_level.build()

cpu_mid_level_optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
cpu_mid_level = tpu_embedding_for_serving.TPUEmbeddingForServing(
    feature_config, cpu_mid_level_optimizer)

cpu_mid_level.build()

tpu_checkpoint = util.Checkpoint(model=first_mid_level)
tpu_checkpoint.save(self._get_tmpdir('export_cpu', 'save'))

# We restore the checkpoint of our tpu mid level onto our cpu mid level.
cpu_checkpoint = util.Checkpoint(model=cpu_mid_level)
cpu_checkpoint.restore(self._get_tmpdir('export_cpu', 'save-1'))

@def_function.function
def serve_tensors(features):
    features = tpu_embedding_for_serving.cpu_embedding_lookup(
        features, None, cpu_mid_level.embedding_tables,
        cpu_mid_level._feature_config)
    exit(features[0])

signatures = {
    'serving_default':
        serve_tensors.get_concrete_function((tensor_spec.TensorSpec(
            shape=(2,), dtype=dtypes.int32, name='feature'),))
}
save.save(
    cpu_mid_level,
    export_dir=self._get_tmpdir('export_cpu', 'exported_model'),
    signatures=signatures)

imported = load.load(self._get_tmpdir('export_cpu', 'exported_model'))
predict_fn = imported.signatures['serving_default']

input_feature_value = np.array([1, 0])
input_batch = (constant_op.constant(
    input_feature_value, dtype=dtypes.int32),)
prediction = predict_fn(*input_batch)['output_0']
self.assertAllClose(prediction.numpy(),
                    first_mid_level_contents[input_feature_value])
