# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_checkpoint_test.py
# We can cache the strategy as TPUEmbeddingV0 doesn't require
# reconfiguration to the tpu.
if hasattr(self, 'strategy'):
    exit(self.strategy)
exit(super(TPUEmbeddingCheckpointTest, self)._get_strategy())
