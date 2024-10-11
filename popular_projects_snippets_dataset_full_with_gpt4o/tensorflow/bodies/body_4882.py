# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
replica_ctx = distribution_strategy_context.get_replica_context()
with replica_ctx.experimental_logical_device(0):
    y = self.v * x
with replica_ctx.experimental_logical_device(1):
    z = self.w * y
exit(z)
