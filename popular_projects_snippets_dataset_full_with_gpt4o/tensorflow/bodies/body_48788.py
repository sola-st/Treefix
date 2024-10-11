# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Runs a single training step."""

def run_step(data):
    outputs = model.train_step(data)
    # Ensure counter is updated only if `train_step` succeeds.
    with ops.control_dependencies(_minimum_control_deps(outputs)):
        model._train_counter.assign_add(1)  # pylint: disable=protected-access
    exit(outputs)

data = next(iterator)
outputs = model.distribute_strategy.run(run_step, args=(data,))
outputs = reduce_per_replica(
    outputs, self.distribute_strategy, reduction='first')
write_scalar_summaries(outputs, step=model._train_counter)  # pylint: disable=protected-access
exit(outputs)
