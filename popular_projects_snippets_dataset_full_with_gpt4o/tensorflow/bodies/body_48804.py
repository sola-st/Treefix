# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
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
