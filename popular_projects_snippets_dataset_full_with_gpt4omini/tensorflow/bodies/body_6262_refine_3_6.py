kwargs = {} # pragma: no cover
class MockDistributionStrategyContext: # pragma: no cover
    @staticmethod# pragma: no cover
    def get_replica_context(): # pragma: no cover
        return None# pragma: no cover
    @staticmethod# pragma: no cover
    def _get_default_replica_context(): # pragma: no cover
        return None# pragma: no cover
# pragma: no cover
distribution_strategy_context = MockDistributionStrategyContext() # pragma: no cover
class MockAutograph: # pragma: no cover
    @staticmethod# pragma: no cover
    def tf_convert(fn, ctx, convert_by_default): # pragma: no cover
        return fn# pragma: no cover
# pragma: no cover
autograph = MockAutograph() # pragma: no cover
class MockAutographContext: # pragma: no cover
    @staticmethod# pragma: no cover
    def control_status_ctx(): # pragma: no cover
        return None# pragma: no cover
# pragma: no cover
autograph_ctx = MockAutographContext() # pragma: no cover
fn = lambda v, *args, **kwargs: v.assign_add(tf.constant(1.0)) # pragma: no cover
class MockSelf:# pragma: no cover
    def _container_strategy(self):# pragma: no cover
        return self# pragma: no cover
    def _update(self, var, fn, args, kwargs, group):# pragma: no cover
        return 'updated'  # Simulated update# pragma: no cover
    def _replica_ctx_update(self, var, fn, args, kwargs, group):# pragma: no cover
        return 'replica_updated'  # Simulated update for replicas# pragma: no cover
self = MockSelf() # pragma: no cover
group = True # pragma: no cover

kwargs = {} # pragma: no cover
class MockDistributionStrategyContext:# pragma: no cover
    @staticmethod# pragma: no cover
    def get_replica_context():# pragma: no cover
        return None# pragma: no cover
    @staticmethod# pragma: no cover
    def _get_default_replica_context():# pragma: no cover
        return None# pragma: no cover
# pragma: no cover
distribution_strategy_context = MockDistributionStrategyContext() # pragma: no cover
class MockAutograph:# pragma: no cover
    @staticmethod# pragma: no cover
    def tf_convert(fn, ctx, convert_by_default):# pragma: no cover
        return fn# pragma: no cover
# pragma: no cover
autograph = MockAutograph() # pragma: no cover
class MockAutographContext:# pragma: no cover
    @staticmethod# pragma: no cover
    def control_status_ctx():# pragma: no cover
        return None# pragma: no cover
# pragma: no cover
autograph_ctx = MockAutographContext() # pragma: no cover
fn = lambda v, *args, **kwargs: v.assign_add(tf.constant(args[0])) # pragma: no cover
class MockSelf:# pragma: no cover
    def _container_strategy(self):# pragma: no cover
        return self# pragma: no cover
    def scope(self):# pragma: no cover
        pass# pragma: no cover
    def _update(self, var, fn, args, kwargs, group):# pragma: no cover
        return 'updated'  # Simulated update# pragma: no cover
    def _replica_ctx_update(self, var, fn, args, kwargs, group):# pragma: no cover
        return 'replica_updated'  # Simulated update for replicas# pragma: no cover
self = MockSelf() # pragma: no cover
args = [1.0] # pragma: no cover
group = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
from l3.Runtime import _l_
"""Run `fn` to update `var` using inputs mirrored to the same devices.

    `tf.distribute.StrategyExtended.update` takes a distributed variable `var`
    to be updated, an update function `fn`, and `args` and `kwargs` for `fn`. It
    applies `fn` to each component variable of `var` and passes corresponding
    values from `args` and `kwargs`. Neither `args` nor `kwargs` may contain
    per-replica values. If they contain mirrored values, they will be unwrapped
    before calling `fn`. For example, `fn` can be `assign_add` and `args` can be
    a mirrored DistributedValues where each component contains the value to be
    added to this mirrored variable `var`. Calling `update` will call
    `assign_add` on each component variable of `var` with the corresponding
    tensor value on that device.

    Example usage:

    ```python
    strategy = tf.distribute.MirroredStrategy(['GPU:0', 'GPU:1']) # With 2
    devices
    with strategy.scope():
      v = tf.Variable(5.0, aggregation=tf.VariableAggregation.SUM)
    def update_fn(v):
      return v.assign(1.0)
    result = strategy.extended.update(v, update_fn)
    # result is
    # Mirrored:{
    #  0: tf.Tensor(1.0, shape=(), dtype=float32),
    #  1: tf.Tensor(1.0, shape=(), dtype=float32)
    # }
    ```

    If `var` is mirrored across multiple devices, then this method implements
    logic as following:

    ```python
    results = {}
    for device, v in var:
      with tf.device(device):
        # args and kwargs will be unwrapped if they are mirrored.
        results[device] = fn(v, *args, **kwargs)
    return merged(results)
    ```

    Otherwise, this method returns `fn(var, *args, **kwargs)` colocated with
    `var`.

    Args:
      var: Variable, possibly mirrored to multiple devices, to operate on.
      fn: Function to call. Should take the variable as the first argument.
      args: Tuple or list. Additional positional arguments to pass to `fn()`.
      kwargs: Dict with keyword arguments to pass to `fn()`.
      group: Boolean. Defaults to True. If False, the return value will be
        unwrapped.

    Returns:
      By default, the merged return value of `fn` across all replicas.  The
      merged result has dependencies to make sure that if it is evaluated at
      all, the side effects (updates) will happen on every replica. If instead
      "group=False" is specified, this function will return a nest of lists
      where each list has an element per replica, and the caller is responsible
      for ensuring all elements are executed.
    """
# TODO(b/178944108): Update the documentation to relfect the fact that
# `update` can be called in a replica context.
if kwargs is None:
    _l_(9587)

    kwargs = {}
    _l_(9586)
replica_context = distribution_strategy_context.get_replica_context()
_l_(9588)
# pylint: disable=protected-access
if (replica_context is None or replica_context is
    distribution_strategy_context._get_default_replica_context()):
    _l_(9593)

    fn = autograph.tf_convert(
        fn, autograph_ctx.control_status_ctx(), convert_by_default=False)
    _l_(9589)
    with self._container_strategy().scope():
        _l_(9591)

        aux = self._update(var, fn, args, kwargs, group)
        _l_(9590)
        exit(aux)
else:
    aux = self._replica_ctx_update(
        var, fn, args=args, kwargs=kwargs, group=group)
    _l_(9592)
    exit(aux)
