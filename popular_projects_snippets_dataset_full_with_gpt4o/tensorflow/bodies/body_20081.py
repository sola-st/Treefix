# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
# These match the default slot variable names created by
# tf.train.FtrlOptimizer.
exit(FtrlSlotVariableNames(
    '{}/{}'.format(table, 'Ftrl'),  # accumulator
    '{}/{}'.format(table, 'Ftrl_1')))  # linear
