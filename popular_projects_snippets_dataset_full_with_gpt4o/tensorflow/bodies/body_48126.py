# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
super(Model, self).__init__(*args, **kwargs)
# initializing _distribution_strategy here since it is possible to call
# predict on a model without compiling it.
self._distribution_strategy = None
self._compile_time_distribution_strategy = None
if (ops.executing_eagerly_outside_functions() and
    distribution_strategy_context.has_strategy()):
    self._set_strategy(
        distribution_strategy_context.get_strategy())

# This flag is used to track if the user is using the deprecated path of
# passing distribution strategy to compile rather than creating the model
# under distribution strategy scope.
self._compile_distribution = False

self._run_eagerly = None
self._experimental_run_tf_function = (
    ops.executing_eagerly_outside_functions())

self._v1_compile_was_called = False
