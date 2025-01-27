# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Context manager to make the strategy current and distribute variables.

    This method returns a context manager, and is used as follows:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> # Variable created inside scope:
    >>> with strategy.scope():
    ...   mirrored_variable = tf.Variable(1.)
    >>> mirrored_variable
    MirroredVariable:{
      0: <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>,
      1: <tf.Variable 'Variable/replica_1:0' shape=() dtype=float32, numpy=1.0>
    }
    >>> # Variable created outside scope:
    >>> regular_variable = tf.Variable(1.)
    >>> regular_variable
    <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>

    _What happens when Strategy.scope is entered?_

    * `strategy` is installed in the global context as the "current" strategy.
      Inside this scope, `tf.distribute.get_strategy()` will now return this
      strategy. Outside this scope, it returns the default no-op strategy.
    * Entering the scope also enters the "cross-replica context". See
      `tf.distribute.StrategyExtended` for an explanation on cross-replica and
      replica contexts.
    * Variable creation inside `scope` is intercepted by the strategy. Each
      strategy defines how it wants to affect the variable creation. Sync
      strategies like `MirroredStrategy`, `TPUStrategy` and
      `MultiWorkerMiroredStrategy` create variables replicated on each replica,
      whereas `ParameterServerStrategy` creates variables on the parameter
      servers. This is done using a custom `tf.variable_creator_scope`.
    * In some strategies, a default device scope may also be entered: in
      `MultiWorkerMiroredStrategy`, a default device scope of "/CPU:0" is
      entered on each worker.

    Note: Entering a scope does not automatically distribute a computation, except
      in the case of high level training framework like keras `model.fit`. If
      you're not using `model.fit`, you
      need to use `strategy.run` API to explicitly distribute that computation.
      See an example in the [custom training loop tutorial](https://www.tensorflow.org/tutorials/distribute/custom_training).


    _What should be in scope and what should be outside?_

    There are a number of requirements on what needs to happen inside the scope.
    However, in places where we have information about which strategy is in use,
    we often enter the scope for the user, so they don't have to do it
    explicitly (i.e. calling those either inside or outside the scope is OK).

    * Anything that creates variables that should be distributed variables
      must be called in a `strategy.scope`. This can be accomplished either by
      directly calling the variable creating function within the scope context,
      or by relying on another API like `strategy.run` or `keras.Model.fit` to
      automatically enter it for you. Any variable that is created outside scope
      will not be distributed and may have performance implications. Some common
      objects that create variables in TF are Models, Optimizers, Metrics. Such
      objects should always be initialized in the scope, and any functions
      that may lazily create variables (e.g., `Model.__call__()`, tracing a
      `tf.function`, etc.) should similarly be called within scope. Another
      source of variable creation can be a checkpoint restore - when variables
      are created lazily. Note that any variable created inside a strategy
      captures the strategy information. So reading and writing to these
      variables outside the `strategy.scope` can also work seamlessly, without
      the user having to enter the scope.
    * Some strategy APIs (such as `strategy.run` and `strategy.reduce`) which
      require to be in a strategy's scope, enter the scope automatically, which
      means when using those APIs you don't need to explicitly enter the scope
      yourself.
    * When a `tf.keras.Model` is created inside a `strategy.scope`, the Model
      object captures the scope information. When high level training framework
      methods such as `model.compile`, `model.fit`, etc. are then called, the
      captured scope will be automatically entered, and the associated strategy
      will be used to distribute the training etc. See a detailed example in
      [distributed keras tutorial](https://www.tensorflow.org/tutorials/distribute/keras).
      WARNING: Simply calling `model(..)` does not automatically enter the
      captured scope -- only high level training framework APIs support this
      behavior: `model.compile`, `model.fit`, `model.evaluate`, `model.predict`
      and `model.save` can all be called inside or outside the scope.
    * The following can be either inside or outside the scope:
        * Creating the input datasets
        * Defining `tf.function`s that represent your training step
        * Saving APIs such as `tf.saved_model.save`. Loading creates variables,
          so that should go inside the scope if you want to train the model in a
          distributed way.
        * Checkpoint saving. As mentioned above - `checkpoint.restore` may
          sometimes need to be inside scope if it creates variables.

    Returns:
      A context manager.
    """
exit(self._extended._scope(self))  # pylint: disable=protected-access
