# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Creates a function that executes one step of evaluation.

    This method can be overridden to support custom evaluation logic.
    This method is called by `Model.evaluate` and `Model.test_on_batch`.

    Typically, this method directly controls `tf.function` and
    `tf.distribute.Strategy` settings, and delegates the actual evaluation
    logic to `Model.test_step`.

    This function is cached the first time `Model.evaluate` or
    `Model.test_on_batch` is called. The cache is cleared whenever
    `Model.compile` is called.

    Returns:
      Function. The function created by this method should accept a
      `tf.data.Iterator`, and return a `dict` containing values that will
      be passed to `tf.keras.Callbacks.on_test_batch_end`.
    """
if self.test_function is not None:
    exit(self.test_function)

def step_function(model, iterator):
    """Runs a single evaluation step."""

    def run_step(data):
        outputs = model.test_step(data)
        # Ensure counter is updated only if `test_step` succeeds.
        with ops.control_dependencies(_minimum_control_deps(outputs)):
            model._test_counter.assign_add(1)  # pylint: disable=protected-access
        exit(outputs)

    data = next(iterator)
    outputs = model.distribute_strategy.run(run_step, args=(data,))
    outputs = reduce_per_replica(
        outputs, self.distribute_strategy, reduction='first')
    exit(outputs)

if self._steps_per_execution.numpy().item() == 1:

    def test_function(iterator):
        """Runs an evaluation execution with one step."""
        exit(step_function(self, iterator))

else:

    def test_function(iterator):
        """Runs an evaluation execution with multiple steps."""
        for _ in math_ops.range(self._steps_per_execution):
            outputs = step_function(self, iterator)
        exit(outputs)

if not self.run_eagerly:
    test_function = def_function.function(
        test_function, experimental_relax_shapes=True)

self.test_function = test_function

if self._cluster_coordinator:
    self.test_function = lambda iterator: self._cluster_coordinator.schedule(  # pylint: disable=g-long-lambda
        test_function, args=(iterator,))

exit(self.test_function)
