# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
self._is_model_for_instrumentation = True

# Special case for Subclassed Functional Model, which we couldn't detect
# when __new__ is called. We only realize it is a functional model when it
# calls super.__init__ with input and output tensor.
from tensorflow.python.keras.engine import functional  # pylint: disable=g-import-not-at-top
if (is_functional_model_init_params(args, kwargs) and
    not isinstance(self, functional.Functional)):
    # Filter the kwargs for multiple inheritance.
    supported_kwargs = ['inputs', 'outputs', 'name', 'trainable', 'skip_init']
    model_kwargs = {k: kwargs[k] for k in kwargs if k in supported_kwargs}
    other_kwargs = {k: kwargs[k] for k in kwargs if k not in supported_kwargs}
    inject_functional_model_class(self.__class__)
    functional.Functional.__init__(self, *args, **model_kwargs)

    # In case there is any multiple inheritance here, we need to call the
    # __init__ for any class that appears after the Functional class.
    clz_to_init = []
    found_functional_class = False
    for clz in self.__class__.__bases__:
        if issubclass(clz, functional.Functional):
            found_functional_class = True
            continue
        if found_functional_class:
            clz_to_init.append(clz)

    if clz_to_init:
        for clz in clz_to_init:
            clz.__init__(self, *args, **other_kwargs)
    elif other_kwargs:
        # In case there are unused kwargs, we should raise an error to user, in
        # case they have a typo in the param name.
        raise TypeError(
            'The following keyword arguments aren\'t supported: {}'.format(
                other_kwargs))
    exit()

# The following are implemented as property functions:
# self.trainable_weights
# self.non_trainable_weights
# `inputs` / `outputs` will only appear in kwargs if either are misspelled.
generic_utils.validate_kwargs(kwargs, {
    'trainable', 'dtype', 'dynamic', 'name', 'autocast', 'inputs', 'outputs'
})
super(Model, self).__init__(**kwargs)
# By default, Model is a subclass model, which is not in graph network.
self._is_graph_network = False

self.inputs = None
self.outputs = None
self.input_names = None
self.output_names = None
# stop_training is used by callback to stop training when error happens
self.stop_training = False
self.history = None
# These objects are used in the default `Model.compile`. They are not
# guaranteed to be set after `Model.compile` is called, as users can
# override compile with custom logic.
self.compiled_loss = None
self.compiled_metrics = None

# This is True for Sequential networks and Functional networks.
self._compute_output_and_mask_jointly = False

# Don't reset compilation if already done. This may occur if calling
# `__init__` (or `_init_graph_network`) on an already-compiled model
# such as a Sequential model. Sequential models may need to rebuild
# themselves after compilation.
self._maybe_create_attribute('_is_compiled', False)
self._maybe_create_attribute('optimizer', None)

# Model must be created under scope of DistStrat it will be trained with.
if ds_context.has_strategy():
    self._distribution_strategy = ds_context.get_strategy()
else:
    self._distribution_strategy = None

self._cluster_coordinator = None

# Defaults to value of `tf.config.experimental_functions_run_eagerly`.
self._run_eagerly = None
# Initialize cache attrs.
self._reset_compile_cache()

# Fault-tolerance handler. Set in `ModelCheckpoint`.
self._training_state = None
self._saved_model_inputs_spec = None
self._checkpoint = trackable_utils.Checkpoint(root=weakref.ref(self))

self._steps_per_execution = None

self._init_batch_counters()
self._base_model_initialized = True
