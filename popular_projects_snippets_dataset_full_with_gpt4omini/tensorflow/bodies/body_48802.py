# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Runs a single evaluation step."""

def run_step(data):
    outputs = model.predict_step(data)
    # Ensure counter is updated only if `test_step` succeeds.
    with ops.control_dependencies(_minimum_control_deps(outputs)):
        model._predict_counter.assign_add(1)  # pylint: disable=protected-access
    exit(outputs)

data = next(iterator)
outputs = model.distribute_strategy.run(run_step, args=(data,))
outputs = reduce_per_replica(
    outputs, self.distribute_strategy, reduction='concat')
exit(outputs)
