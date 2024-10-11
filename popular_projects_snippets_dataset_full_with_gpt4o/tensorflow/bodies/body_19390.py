# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py
with self.assertRaisesRegex(
    ValueError, 'Multiple tables with name table found.'):
    with self._get_strategy().scope():
        tpu_embedding_v2.TPUEmbedding(
            (tpu_embedding_v2_utils.FeatureConfig(
                table=tpu_embedding_v2_utils.TableConfig(
                    name='table',
                    vocabulary_size=4,
                    dim=2,
                    initializer=self.initializer,),
                name='watched'),
             tpu_embedding_v2_utils.FeatureConfig(
                 table=tpu_embedding_v2_utils.TableConfig(
                     name='table',
                     vocabulary_size=4,
                     dim=2,
                     initializer=self.initializer),
                 name='favorited')),
            tpu_embedding_v2_utils.SGD(learning_rate=0.1))
