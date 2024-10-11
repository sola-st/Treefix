# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
self._instrument_layer_creation()

# These properties should be set by the user via keyword arguments.
# note that 'dtype', 'input_shape' and 'batch_input_shape'
# are only applicable to input layers: do not pass these keywords
# to non-input layers.
allowed_kwargs = {
    'input_dim',
    'input_shape',
    'batch_input_shape',
    'batch_size',
    'weights',
    'activity_regularizer',
    'autocast',
    'implementation',
}
# Validate optional keyword arguments.
generic_utils.validate_kwargs(kwargs, allowed_kwargs)

# Mutable properties
# Indicates whether the layer's weights are updated during training
# and whether the layer's updates are run during training.
self._trainable = trainable
# A stateful layer is a layer whose updates are run during inference too,
# for instance stateful RNNs.
self._stateful = False
# Indicates whether `build` needs to be called upon layer call, to create
# the layer's weights.
self.built = False
# Provides information about which inputs are compatible with the layer.
self._input_spec = None

# SavedModel-related attributes.
# Record the build input shape for loading purposes.
# TODO(kathywu): Move this to Layer._set_save_spec once cl/290121460 is
# submitted.
self._build_input_shape = None
self._saved_model_inputs_spec = None

# `Layer.compute_mask` will be called at the end of `Layer.__call__` if
# `Layer.compute_mask` is overridden, or if the `Layer` subclass sets
# `self.supports_masking=True`.
self._supports_masking = not generic_utils.is_default(self.compute_mask)

self._init_set_name(name)
self._activity_regularizer = regularizers.get(
    kwargs.pop('activity_regularizer', None))
self._maybe_create_attribute('_trainable_weights', [])
self._maybe_create_attribute('_non_trainable_weights', [])
self._updates = []
# Object to store all thread local layer properties.
self._thread_local = threading.local()
# A list of zero-argument lambdas which return Tensors, used for variable
# regularizers.
self._callable_losses = []
# A list of symbolic Tensors containing activity regularizers and losses
# manually added through `add_loss` in graph-building mode.
self._losses = []
# A list of metric instances corresponding to the symbolic metric tensors
# added using the `add_metric` API.
self._metrics = []
# Ensures the same metric is not added multiple times in `MirroredStrategy`.
self._metrics_lock = threading.Lock()

# Both graph and subclassed networks have a dtype policy. For graph
# networks, the policy's compute and variable dtypes are ignored. Such
# networks only use the policy if it is a PolicyV1, in which case it uses
# the PolicyV1's loss_scale (Policy does not have a loss_scale). For
# subclassed networks, the compute and variable dtypes are used as like any
# ordinary layer.
self._set_dtype_policy(dtype)
# Boolean indicating whether the layer automatically casts its inputs to the
# layer's compute_dtype.
self._autocast = kwargs.get('autocast',
                            base_layer_utils.v2_dtype_behavior_enabled())

# Tracks `TrackableDataStructure`s, `Module`s, and `Layer`s.
# Ordered by when the object was assigned as an attr.
# Entries are unique.
self._maybe_create_attribute('_self_tracked_trackables', [])

# These lists will be filled via successive calls
# to self._add_inbound_node().
# Used in symbolic mode only, only in conjunction with graph-networks
self._inbound_nodes_value = []
self._outbound_nodes_value = []

self._init_call_fn_args()

# Whether the `call` method can be used to build a TF graph without issues.
# This attribute has no effect if the model is created using the Functional
# API. Instead, `model.dynamic` is determined based on the internal layers.
self._dynamic = dynamic

# Manage input shape information if passed.
if 'input_dim' in kwargs and 'input_shape' not in kwargs:
    # Backwards compatibility: alias 'input_dim' to 'input_shape'.
    kwargs['input_shape'] = (kwargs['input_dim'],)
if 'input_shape' in kwargs or 'batch_input_shape' in kwargs:
    # In this case we will later create an input layer
    # to insert before the current layer
    if 'batch_input_shape' in kwargs:
        batch_input_shape = tuple(kwargs['batch_input_shape'])
    elif 'input_shape' in kwargs:
        if 'batch_size' in kwargs:
            batch_size = kwargs['batch_size']
        else:
            batch_size = None
        batch_input_shape = (batch_size,) + tuple(kwargs['input_shape'])
    self._batch_input_shape = batch_input_shape

# Manage initial weight values if passed.
self._initial_weights = kwargs.get('weights', None)

# Whether the layer will track any layers that is set as attribute on itself
# as sub-layers, the weights from the sub-layers will be included in the
# parent layer's variables() as well.
# Default to True, which means auto tracking is turned on. Certain subclass
# might want to turn it off, like Sequential model.
self._auto_track_sub_layers = True

# For backwards compat reasons, most built-in layers do not guarantee
# That they will 100% preserve the structure of input args when saving
# / loading configs. E.g. they may un-nest an arg that is
# a list with one element.
self._preserve_input_structure_in_config = False
