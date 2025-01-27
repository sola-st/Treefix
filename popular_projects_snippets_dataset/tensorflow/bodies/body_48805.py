# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Creates a function that executes one step of inference.

    This method can be overridden to support custom inference logic.
    This method is called by `Model.predict` and `Model.predict_on_batch`.

    Typically, this method directly controls `tf.function` and
    `tf.distribute.Strategy` settings, and delegates the actual evaluation
    logic to `Model.predict_step`.

    This function is cached the first time `Model.predict` or
    `Model.predict_on_batch` is called. The cache is cleared whenever
    `Model.compile` is called.

    Returns:
      Function. The function created by this method should accept a
      `tf.data.Iterator`, and return the outputs of the `Model`.
    """
if self.predict_function is not None:
    exit(self.predict_function)

def step_function(model, iterator):
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

if (self._steps_per_execution is None or
    self._steps_per_execution.numpy().item() == 1):

    def predict_function(iterator):
        """Runs an evaluation execution with one step."""
        exit(step_function(self, iterator))

else:

    def predict_function(iterator):
        """Runs an evaluation execution with multiple steps."""
        outputs = step_function(self, iterator)
        for _ in math_ops.range(self._steps_per_execution - 1):
            directives.set_loop_options(
                shape_invariants=[(
                    t, tf_utils.get_tensor_spec(t, dynamic_batch=True).shape)
                                  for t in nest.flatten(outputs)])
            step_outputs = step_function(self, iterator)
            outputs = nest.map_structure(lambda t1, t2: concat([t1, t2]), outputs,
                                         step_outputs)
        exit(outputs)

if not self.run_eagerly:
    predict_function = def_function.function(
        predict_function, experimental_relax_shapes=True)

self.predict_function = predict_function
exit(self.predict_function)
