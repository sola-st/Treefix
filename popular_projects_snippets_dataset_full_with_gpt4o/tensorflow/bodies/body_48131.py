# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Configures the model for training.

    Args:
        optimizer: String (name of optimizer) or optimizer instance.
            See `tf.keras.optimizers`.
        loss: String (name of objective function), objective function or
            `tf.keras.losses.Loss` instance. See `tf.keras.losses`. An objective
            function is any callable with the signature
            `scalar_loss = fn(y_true, y_pred)`. If the model has multiple
            outputs, you can use a different loss on each output by passing a
            dictionary or a list of losses. The loss value that will be
            minimized by the model will then be the sum of all individual
            losses.
        metrics: List of metrics to be evaluated by the model during training
            and testing. Typically you will use `metrics=['accuracy']`.
            To specify different metrics for different outputs of a
            multi-output model, you could also pass a dictionary, such as
            `metrics={'output_a': 'accuracy', 'output_b': ['accuracy', 'mse']}`.
            You can also pass a list (len = len(outputs)) of lists of metrics
            such as `metrics=[['accuracy'], ['accuracy', 'mse']]` or
            `metrics=['accuracy', ['accuracy', 'mse']]`.
        loss_weights: Optional list or dictionary specifying scalar
            coefficients (Python floats) to weight the loss contributions
            of different model outputs.
            The loss value that will be minimized by the model
            will then be the *weighted sum* of all individual losses,
            weighted by the `loss_weights` coefficients.
            If a list, it is expected to have a 1:1 mapping
            to the model's outputs. If a tensor, it is expected to map
            output names (strings) to scalar coefficients.
        sample_weight_mode: If you need to do timestep-wise
            sample weighting (2D weights), set this to `"temporal"`.
            `None` defaults to sample-wise weights (1D).
            If the model has multiple outputs, you can use a different
            `sample_weight_mode` on each output by passing a
            dictionary or a list of modes.
        weighted_metrics: List of metrics to be evaluated and weighted
            by sample_weight or class_weight during training and testing.
        target_tensors: By default, Keras will create placeholders for the
            model's target, which will be fed with the target data during
            training. If instead you would like to use your own
            target tensors (in turn, Keras will not expect external
            Numpy data for these targets at training time), you
            can specify them via the `target_tensors` argument. It can be
            a single tensor (for a single-output model), a list of tensors,
            or a dict mapping output names to target tensors.
        distribute: NOT SUPPORTED IN TF 2.0, please create and compile the
            model under distribution strategy scope instead of passing it to
            compile.
        **kwargs: Any additional arguments.

    Raises:
        ValueError: In case of invalid arguments for
            `optimizer`, `loss`, `metrics` or `sample_weight_mode`.
    """
self._assert_built_as_v1()
self._run_eagerly = kwargs.pop('run_eagerly', None)
self._experimental_run_tf_function = kwargs.pop(
    'experimental_run_tf_function', True)
self._v1_compile_was_called = True

# Prepare Session arguments (legacy).
kwargs.pop('cloning', None)  # Legacy DistStrat argument, never used.
self._from_serialized = kwargs.pop('from_serialized', False)
allowed_kwargs = {'feed_dict', 'fetches', 'options', 'run_metadata'}
unknown_kwargs = set(kwargs.keys()) - allowed_kwargs
if unknown_kwargs:
    raise TypeError(
        'Invalid keyword argument(s) in `compile`: %s' % (unknown_kwargs,))
self._function_kwargs = kwargs
if self._function_kwargs:
    self._experimental_run_tf_function = False
    if self.run_eagerly:
        raise ValueError(
            'Session keyword arguments are not supported '
            'when `run_eagerly=True`. You passed the following '
            'Session arguments: %s' % (self._function_kwargs,))

self._set_optimizer(optimizer)
is_any_keras_optimizer_v1 = any(
    (isinstance(opt, optimizer_v1.Optimizer)
     and not isinstance(opt, optimizer_v1.TFOptimizer)
    ) for opt in nest.flatten(self.optimizer))

if is_any_keras_optimizer_v1 and ops.executing_eagerly_outside_functions():
    raise ValueError('`tf.compat.v1.keras` Optimizer (', optimizer, ') is '
                     'not supported when eager execution is enabled. Use a '
                     '`tf.keras` Optimizer instead, or disable eager '
                     'execution.')

if ((target_tensors is not None)
    or not ops.executing_eagerly_outside_functions()):
    # Fallback out of things that aren't supported with v2 loops
    self._experimental_run_tf_function = False

if distribute is not None:
    if tf2.enabled() or self._experimental_run_tf_function:
        raise ValueError(
            'Distribute argument in compile is not available in TF 2.0 please '
            'create the model under the distribution strategy scope.')
    logging.warning('Distribute argument in compile is deprecated please '
                    'create the model under the distribution strategy scope.')
    self._distribution_strategy = distribute
    self._compile_distribution = True
else:
    if distribution_strategy_context.has_strategy():
        # When the user builds the model in the DS scope and cross replica
        # context we want distribution strategy to be set but when building the
        # replica copies of the models internally we should not be compiling
        # with distribution strategy and use the default compilation path.
        if distribution_strategy_context.in_cross_replica_context():
            self._distribution_strategy = (
                distribution_strategy_context.get_strategy())

if isinstance(self._distribution_strategy,
              parameter_server_strategy.ParameterServerStrategyV1):
    raise NotImplementedError(
        '`tf.compat.v1.distribute.experimental.ParameterServerStrategy` '
        'currently only works with the tf.Estimator API')

if isinstance(self._distribution_strategy,
              parameter_server_strategy_v2.ParameterServerStrategyV2):
    raise NotImplementedError(
        '`tf.distribute.experimental.ParameterServerStrategy` is only '
        'supported in TF2.')

if not self._experimental_run_tf_function:
    self._validate_compile_param_for_distribution_strategy(self.run_eagerly,
                                                           sample_weight_mode,
                                                           target_tensors,
                                                           weighted_metrics)
# We've disabled automatic dependency tracking for this method, but do want
# to add a checkpoint dependency on the optimizer if it's trackable.
if isinstance(self.optimizer, trackable.Trackable):
    self._track_trackable(
        self.optimizer, name='optimizer', overwrite=True)
self.loss = loss or {}
self.loss_weights = loss_weights
self.sample_weight_mode = sample_weight_mode
self._compile_metrics = metrics or []
self._compile_weighted_metrics = weighted_metrics
if self.run_eagerly and target_tensors is not None:
    raise ValueError(
        'target_tensors argument is not supported when '
        'running a model eagerly.')

# _training_endpoints contains a list of _TrainingEndpoint object, which has
# all the model output/target/loss and related metadata.
self._training_endpoints = []

# Used to freeze the behavior of the Model once `compile` has been called.
self._compiled_trainable_state = self._get_trainable_state()

# Set tf.distribute.Strategy specific parameters.
self._distributed_model_cache = {}
self._distributed_function_cache = {}

# Clear any `_eager_losses` that was added.
self._clear_losses()

if (not context.executing_eagerly() and
    self._distribution_strategy is not None):
    # Ensures a Session is created and configured correctly for Distribution
    # Strategy.
    backend.configure_and_create_distributed_session(
        self._distribution_strategy)
# Initialize model metric attributes.
self._init_metric_attributes()
if not self.built or not self.inputs or not self.outputs:
    # Model is not compilable because it does not know its number of inputs
    # and outputs, nor their shapes and names. We will compile after the first
    # time the model gets called on training data.
    exit()
self._is_compiled = True

# Prepare list of loss functions, same size of model outputs.
self.loss_functions = training_utils_v1.prepare_loss_functions(
    self.loss, self.output_names)

target_tensors = self._process_target_tensor_for_compile(target_tensors)

for o, n, l, t in zip(self.outputs, self.output_names,
                      self.loss_functions, target_tensors):
    endpoint = _TrainingEndpoint(o, n, l)
    endpoint.create_training_target(t, run_eagerly=self.run_eagerly)
    self._training_endpoints.append(endpoint)

# Prepare list loss weights, same size of model outputs.
training_utils_v1.prepare_loss_weights(self._training_endpoints,
                                       loss_weights)

# Initialization for Eager mode execution.
if self.run_eagerly:
    self._compile_eagerly(metrics, weighted_metrics, sample_weight_mode)
    exit()

with backend.get_graph().as_default():
    # Save all metric attributes per output of the model.
    self._cache_output_metric_attributes(metrics, weighted_metrics)

    # Set metric attributes on model.
    self._set_metric_attributes()

    # Invoke metric functions (unweighted) for all the outputs.
    self._handle_metrics(
        self.outputs,
        targets=self._targets,
        skip_target_masks=self._prepare_skip_target_masks(),
        masks=self._prepare_output_masks())

    # Prepare sample weight modes. List with the same length as model outputs.
    training_utils_v1.prepare_sample_weight_modes(
        self._training_endpoints, sample_weight_mode)

    # Creates the model loss and weighted metrics sub-graphs.
    self._compile_weights_loss_and_weighted_metrics()

    # Functions for train, test and predict will
    # be compiled lazily when required.
    # This saves time when the user is not using all functions.
    self.train_function = None
    self.test_function = None
    self.predict_function = None

    # Collected trainable weights, sorted in topological order.
    self._collected_trainable_weights = self.trainable_weights

    # Validate all variables were correctly created in distribution scope.
    if self._distribution_strategy and not self._compile_distribution:
        for v in self.variables:
            strategy = self._distribution_strategy
            if not strategy.extended.variable_created_in_scope(v):
                raise ValueError(
                    'Variable (%s) was not created in the distribution strategy '
                    'scope of (%s). It is most likely due to not all layers or '
                    'the model or optimizer being created outside the distribution '
                    'strategy scope. Try to make sure your code looks similar '
                    'to the following.\n'
                    'with strategy.scope():\n'
                    '  model=_create_model()\n'
                    '  model.compile(...)'% (v, strategy))
