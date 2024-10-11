# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py
if hasattr(self, 'strategy'):
    exit(self.strategy)
exit(super(TPUEmbeddingV0CorrectnessTest, self)._get_strategy())
