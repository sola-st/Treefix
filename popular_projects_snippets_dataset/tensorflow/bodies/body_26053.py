# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
if pb.WhichOneof("optional_deterministic") is not None:
    self.deterministic = pb.deterministic
self.autotune._from_proto(pb.autotune_options)  # pylint: disable=protected-access
self.experimental_distribute._from_proto(pb.distribute_options)  # pylint: disable=protected-access
if pb.WhichOneof("optional_external_state_policy") is not None:
    self.experimental_external_state_policy = (
        ExternalStatePolicy._from_proto(  # pylint: disable=protected-access
            pb.external_state_policy))
self.experimental_optimization._from_proto(pb.optimization_options)  # pylint: disable=protected-access
if pb.WhichOneof("optional_slack") is not None:
    self.experimental_slack = pb.slack
if pb.WhichOneof("optional_symbolic_checkpoint") is not None:
    self.experimental_symbolic_checkpoint = pb.symbolic_checkpoint
self.threading._from_proto(pb.threading_options)  # pylint: disable=protected-access
