# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
predict = math_ops.matmul(batch_features, w)
exit(predict)
