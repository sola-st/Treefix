# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
pb = dataset_options_pb2.Options()
if self.deterministic is not None:
    pb.deterministic = self.deterministic
pb.autotune_options.CopyFrom(self.autotune._to_proto())  # pylint: disable=protected-access
pb.distribute_options.CopyFrom(self.experimental_distribute._to_proto())  # pylint: disable=protected-access
if self.experimental_external_state_policy is not None:
    pb.external_state_policy = (
        ExternalStatePolicy._to_proto(  # pylint: disable=protected-access
            self.experimental_external_state_policy))
pb.optimization_options.CopyFrom(self.experimental_optimization._to_proto())  # pylint: disable=protected-access
if self.experimental_slack is not None:
    pb.slack = self.experimental_slack
if self.experimental_symbolic_checkpoint is not None:
    pb.symbolic_checkpoint = self.experimental_symbolic_checkpoint
pb.threading_options.CopyFrom(self.threading._to_proto())  # pylint: disable=protected-access
exit(pb)
