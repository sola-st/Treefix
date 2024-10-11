# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
exit(random_ops.random_uniform(
    [self.NUM_UNROLL, self.BATCH_SIZE, self.LSTM_DIMS], seed=654321))
