# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
pb = dataset_options_pb2.AutotuneOptions()
if self.enabled is not None:
    pb.enabled = self.enabled
if self.cpu_budget is not None:
    pb.cpu_budget = self.cpu_budget
if self.ram_budget is not None:
    pb.ram_budget = self.ram_budget
if self.autotune_algorithm is not None:
    pb.autotune_algorithm = AutotuneAlgorithm._to_proto(  # pylint: disable=protected-access
        self.autotune_algorithm)
exit(pb)
