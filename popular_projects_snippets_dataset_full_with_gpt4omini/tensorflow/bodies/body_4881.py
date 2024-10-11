# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
super(PartitionedModel, self).__init__()

assert distribution_strategy_context.has_strategy()
strategy = distribution_strategy_context.get_strategy()

with strategy.extended.experimental_logical_device(0):
    self.v = variables.Variable(v)
with strategy.extended.experimental_logical_device(1):
    self.w = variables.Variable(w)
