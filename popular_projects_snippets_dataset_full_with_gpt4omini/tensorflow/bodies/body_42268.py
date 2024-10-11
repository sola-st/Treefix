# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
level = self.config.graph_options.optimizer_options.global_jit_level
exit((level == config_pb2.OptimizerOptions.ON_1 or
        level == config_pb2.OptimizerOptions.ON_2))
