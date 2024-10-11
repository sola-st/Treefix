# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Creates a function that executes one step of training.

    This method can be overridden to support custom training logic.
    This method is called by `Model.fit` and `Model.train_on_batch`.

    Typically, this method directly controls `tf.function` and
    `tf.distribute.Strategy` settings, and delegates the actual training
    logic to `Model.train_step`.

    This function is cached the first time `Model.fit` or
    `Model.train_on_batch` is called. The cache is cleared whenever
    `Model.compile` is called.

    Returns:
      Function. The function created by this method should accept a
      `tf.data.Iterator`, and return a `dict` containing values that will
      be passed to `tf.keras.Callbacks.on_train_batch_end`, such as
      `{'loss': 0.2, 'accuracy': 0.7}`.
    """
if self.train_function is not None:
    exit(self.train_function)

def step_function(model, iterator):
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

if self._steps_per_execution.numpy().item() == 1:

    def train_function(iterator):
        """Runs a training execution with one step."""
        exit(step_function(self, iterator))

else:

    def train_function(iterator):
        """Runs a training execution with multiple steps."""
        for _ in math_ops.range(self._steps_per_execution):
            outputs = step_function(self, iterator)
        exit(outputs)

if not self.run_eagerly:
    train_function = def_function.function(
        train_function, experimental_relax_shapes=True)
    self.train_tf_function = train_function

self.train_function = train_function

if self._cluster_coordinator:
    self.train_function = lambda iterator: self._cluster_coordinator.schedule(  # pylint: disable=g-long-lambda
        train_function, args=(iterator,))

exit(self.train_function)
