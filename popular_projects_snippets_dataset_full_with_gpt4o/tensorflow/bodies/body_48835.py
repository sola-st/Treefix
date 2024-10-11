# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Performs validation checks for the default `compile`."""
if any(
    isinstance(opt, optimizer_v1.Optimizer)
    for opt in nest.flatten(optimizer)):
    raise ValueError(
        '`tf.compat.v1.keras` Optimizer (', optimizer, ') is '
        'not supported when eager execution is enabled. Use a '
        '`tf.keras` Optimizer instead, or disable eager '
        'execution.')

kwargs.pop('cloning', None)  # Legacy DistStrat argument, never used.
kwargs.pop('experimental_run_tf_function', None)  # Always `True`.
if kwargs.pop('distribute', None) is not None:
    raise ValueError(
        'Distribute argument in compile is not available in TF 2.0 please '
        'create the model under the distribution strategy scope.')
if kwargs.pop('target_tensors', None) is not None:
    raise ValueError(
        'target_tensors argument is not supported when executing eagerly.')
invalid_kwargs = set(kwargs) - {'sample_weight_mode'}
if invalid_kwargs:
    raise TypeError('Invalid keyword argument(s) in `compile`: %s' %
                    (invalid_kwargs,))

# Model must be created and compiled with the same DistStrat.
if self.built and ds_context.has_strategy():
    strategy = ds_context.get_strategy()
    for v in self.variables:
        if not strategy.extended.variable_created_in_scope(v):
            raise ValueError(
                'Variable (%s) was not created in the distribution strategy '
                'scope of (%s). It is most likely due to not all layers or '
                'the model or optimizer being created outside the distribution '
                'strategy scope. Try to make sure your code looks similar '
                'to the following.\n'
                'with strategy.scope():\n'
                '  model=_create_model()\n'
                '  model.compile(...)' % (v, strategy))

    # Model metrics must be created in the same distribution strategy scope
    # as the model.
strategy = self.distribute_strategy
for metric in nest.flatten(metrics):
    for v in getattr(metric, 'variables', []):
        if not strategy.extended.variable_created_in_scope(v):
            raise ValueError(
                'Metric (%s) passed to model.compile was created inside of a '
                'different distribution strategy scope than the model. All '
                'metrics must be created in the same distribution strategy '
                'scope as the model (in this case %s). If you pass in a string '
                'identifier for a metric to compile the metric will '
                'automatically be created in the correct distribution '
                'strategy scope.' % (metric, strategy)
            )

    # Model metrics must be created in the same distribution strategy scope
    # as the model.
for opt in nest.flatten(optimizer):
    for v in getattr(opt, '_weights', []):
        if not strategy.extended.variable_created_in_scope(v):
            raise ValueError(
                'Optimizer (%s) passed to model.compile was created inside of a '
                'different distribution strategy scope than the model. All '
                'optimizers must be created in the same distribution strategy '
                'scope as the model (in this case %s). If you pass in a string '
                'identifier for an optimizer to compile the optimizer will '
                'automatically be created in the correct distribution '
                'strategy scope.' % (opt, strategy))
