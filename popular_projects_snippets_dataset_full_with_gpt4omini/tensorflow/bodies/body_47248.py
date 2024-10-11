# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Creates a function to run one step of distributed model execution."""
strategy = model._distribution_strategy

with strategy.scope():
    per_replica_function = _make_replica_execution_function(model, mode)

    def distributed_function(input_fn):
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

    if not model.run_eagerly:
        distributed_function = def_function.function(distributed_function)
        def execution_function(input_fn):
            # `numpy` translates Tensors to values in Eager mode.
            exit([out.numpy() for out in distributed_function(input_fn)])
    else:
        execution_function = distributed_function

    exit(execution_function)
