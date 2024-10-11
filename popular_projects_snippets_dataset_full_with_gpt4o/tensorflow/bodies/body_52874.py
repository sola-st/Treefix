# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
raise ValueError('SharedEmbeddingColumns are not supported in '
                 '`linear_model` or `input_layer`. Please use '
                 '`DenseFeatures` or `LinearModel` instead.')
