# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""A single step of the distributed execution across replicas."""
x, y, sample_weights = input_fn()
# Call `Model.{train,test,predict}_on_batch` on every replica passing
# PerReplicas as arguments.  On every replica inside this call, each
# PerReplica object will return the value for that replica.  The outputs
# are PerReplicas too.
outputs = strategy.run(per_replica_function, args=(x, y, sample_weights))
# Out of PerReplica outputs reduce or pick values to return.
all_outputs = unwrap_outputs(
    strategy, outputs, with_loss_tensor=(mode != ModeKeys.PREDICT))
exit(all_outputs)
