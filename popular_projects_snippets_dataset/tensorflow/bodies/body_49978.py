# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Create a new Optimizer.

    This must be called by the constructors of subclasses.
    Note that Optimizer instances should not bind to a single graph,
    and so shouldn't keep Tensors as member variables. Generally
    you should be able to use the _set_hyper()/state.get_hyper()
    facility instead.

    This class is stateful and thread-compatible.

    Example of custom gradient transformations:

    ```python
    def my_gradient_transformer(grads_and_vars):
      # Simple example, double the gradients.
      return [(2. * g, v) for g, v in grads_and_vars]

    optimizer = tf.keras.optimizers.SGD(
        1e-3, gradient_transformers=[my_gradient_transformer])
    ```

    Args:
      name: String. The name to use for momentum accumulator weights created
        by the optimizer.
      gradient_aggregator: The function to use to aggregate gradients across
        devices (when using `tf.distribute.Strategy`). If `None`, defaults to
        summing the gradients across devices. The function should accept and
        return a list of `(gradient, variable)` tuples.
      gradient_transformers: Optional. List of functions to use to transform
        gradients before applying updates to Variables. The functions are
        applied after `gradient_aggregator`. The functions should accept and
        return a list of `(gradient, variable)` tuples.
      **kwargs: keyword arguments. Allowed arguments are `clipvalue`,
        `clipnorm`, `global_clipnorm`.
        If `clipvalue` (float) is set, the gradient of each weight
        is clipped to be no higher than this value.
        If `clipnorm` (float) is set, the gradient of each weight
        is individually clipped so that its norm is no higher than this value.
        If `global_clipnorm` (float) is set the gradient of all weights is
        clipped so that their global norm is no higher than this value.

    Raises:
      ValueError: in case of any invalid argument.
    """
allowed_kwargs = {"clipnorm", "clipvalue", "lr", "decay", "global_clipnorm"}
for k in kwargs:
    if k not in allowed_kwargs:
        raise TypeError("Unexpected keyword argument "
                        "passed to optimizer: " + str(k))
    # checks that all keyword arguments are non-negative.
    if kwargs[k] is not None and kwargs[k] < 0:
        raise ValueError("Expected {} >= 0, received: {}".format(k, kwargs[k]))
    if k == "lr":
        warnings.warn(
            "The `lr` argument is deprecated, use `learning_rate` instead.")

self._use_locking = True
self._init_set_name(name)
self._hyper = {}
# dict: {variable name : {slot name : variable}}
self._slots = {}
self._slot_names = []
self._weights = []
self._iterations = None

# For implementing Trackable. Stores information about how to restore
# slot variables which have not yet been created
# (trackable._CheckpointPosition objects).
#  {slot_name :
#      {_var_key(variable_to_train): [checkpoint_position, ... ], ... },
#   ... }
self._deferred_slot_restorations = {}

decay = kwargs.pop("decay", 0.0)
if decay < 0.:
    raise ValueError("decay cannot be less than 0: {}".format(decay))
self._initial_decay = decay

self._hypers_created = False
# Store the distribution strategy object if the optimizer is created inside
# strategy scope, so it could be used to create variables later.
if distribute_ctx.has_strategy():
    self._distribution_strategy = distribute_ctx.get_strategy()
else:
    self._distribution_strategy = None

# Configure gradient transformations.
if gradient_aggregator is None:
    gradient_aggregator = optimizer_utils.all_reduce_sum_gradients
self.gradient_aggregator = gradient_aggregator
if gradient_transformers is None:
    gradient_transformers = []
self.gradient_transformers = gradient_transformers
self.clipnorm = kwargs.pop("clipnorm", None)
self.global_clipnorm = kwargs.pop("global_clipnorm", None)
if self.clipnorm is not None and self.global_clipnorm is not None:
    raise ValueError("Cannot accept both `clipnorm` and `global_clipnorm`, "
                     "passed `clipnorm` {}, `global_clipnorm` {}".format(
                         self.clipnorm, self.global_clipnorm))
self.clipvalue = kwargs.pop("clipvalue", None)
