# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
if pb.WhichOneof("optional_enabled") is not None:
    self.enabled = pb.enabled
if pb.WhichOneof("optional_cpu_budget") is not None:
    self.cpu_budget = pb.cpu_budget
if pb.WhichOneof("optional_ram_budget") is not None:
    self.ram_budget = pb.ram_budget
if pb.WhichOneof("optional_autotune_algorithm") is not None:
    self.autotune_algorithm = AutotuneAlgorithm._from_proto(  # pylint: disable=protected-access
        pb.autotune_algorithm)
