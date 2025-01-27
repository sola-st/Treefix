# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
if isinstance(variable, tpu_embedding_v2.TPUEmbeddingVariable):
    exit(variable.variables[0])
exit(variable)
