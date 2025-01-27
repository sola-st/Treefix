# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Computes the (weighted) mean of the given values.

  The `mean` function creates two local variables, `total` and `count`
  that are used to compute the average of `values`. This average is ultimately
  returned as `mean` which is an idempotent operation that simply divides
  `total` by `count`.

  For estimation of the metric over a stream of data, the function creates an
  `update_op` operation that updates these variables and returns the `mean`.
  `update_op` increments `total` with the reduced sum of the product of `values`
  and `weights`, and it increments `count` with the reduced sum of `weights`.

  If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

  Args:
    values: A `Tensor` of arbitrary dimensions.
    weights: Optional `Tensor` whose rank is either 0, or the same rank as
      `values`, and must be broadcastable to `values` (i.e., all dimensions must
      be either `1`, or the same as the corresponding `values` dimension).
    metrics_collections: An optional list of collections that `mean`
      should be added to.
    updates_collections: An optional list of collections that `update_op`
      should be added to.
    name: An optional variable_scope name.

  Returns:
    mean: A `Tensor` representing the current mean, the value of `total` divided
      by `count`.
    update_op: An operation that increments the `total` and `count` variables
      appropriately and whose value matches `mean_value`.

  Raises:
    ValueError: If `weights` is not `None` and its shape doesn't match `values`,
      or if either `metrics_collections` or `updates_collections` are not a list
      or tuple.
    RuntimeError: If eager execution is enabled.

  @compatibility(TF2)
  `tf.compat.v1.metrics.mean` is not compatible with eager
  execution or `tf.function`.
  Please use `tf.keras.metrics.Mean` instead for TF2 migration. After
  instantiating a `tf.keras.metrics.Mean` object, you can first call the
  `update_state()` method to record the new values, and then call the
  `result()` method to get the mean eagerly. You can also attach it to a
  Keras model with the `add_metric` method.  Please refer to the [migration
  guide](https://www.tensorflow.org/guide/migrate#new-style_metrics_and_losses)
  for more details.

  #### Structural Mapping to TF2

  Before:

  ```python
  mean, update_op = tf.compat.v1.metrics.mean(
    values=values,
    weights=weights,
    metrics_collections=metrics_collections,
    update_collections=update_collections,
    name=name)
  ```

  After:

  ```python
   m = tf.keras.metrics.Mean(
     name=name)

   m.update_state(
     values=values,
     sample_weight=weights)

   mean = m.result()
  ```

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name    | Note                       |
  | :-------------------- | :-------------- | :------------------------- |
  | `values`              | `values`        | In `update_state()` method |
  | `weights`             | `sample_weight` | In `update_state()` method |
  | `metrics_collections` | Not supported   | Metrics should be tracked  |
  :                       :                 : explicitly or with Keras   :
  :                       :                 : APIs, for example,         :
  :                       :                 : [add_metric][add_metric],  :
  :                       :                 : instead of via collections :
  | `updates_collections` | Not supported   | -                          |
  | `name`                | `name`          | In constructor             |

  [add_metric]:https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer#add_metric


  #### Before & After Usage Example

  Before:

  >>> g = tf.Graph()
  >>> with g.as_default():
  ...   values = [1, 2, 3]
  ...   mean, update_op = tf.compat.v1.metrics.mean(values)
  ...   global_init = tf.compat.v1.global_variables_initializer()
  ...   local_init = tf.compat.v1.local_variables_initializer()
  >>> sess = tf.compat.v1.Session(graph=g)
  >>> sess.run([global_init, local_init])
  >>> sess.run(update_op)
  >>> sess.run(mean)
  2.0


  After:

  >>> m = tf.keras.metrics.Mean()
  >>> m.update_state([1, 2, 3])
  >>> m.result().numpy()
  2.0

  ```python
  # Used within Keras model
  model.add_metric(tf.keras.metrics.Mean()(values))
  ```

  @end_compatibility
  """
if context.executing_eagerly():
    raise RuntimeError('tf.metrics.mean is not supported when eager execution '
                       'is enabled.')

with variable_scope.variable_scope(name, 'mean', (values, weights)):
    values = math_ops.cast(values, dtypes.float32)

    total = metric_variable([], dtypes.float32, name='total')
    count = metric_variable([], dtypes.float32, name='count')

    if weights is None:
        num_values = math_ops.cast(array_ops.size(values), dtypes.float32)
    else:
        values, _, weights = _remove_squeezable_dimensions(
            predictions=values, labels=None, weights=weights)
        weights = weights_broadcast_ops.broadcast_weights(
            math_ops.cast(weights, dtypes.float32), values)
        values = math_ops.multiply(values, weights)
        num_values = math_ops.reduce_sum(weights)

    update_total_op = state_ops.assign_add(total, math_ops.reduce_sum(values))
    with ops.control_dependencies([values]):
        update_count_op = state_ops.assign_add(count, num_values)

    def compute_mean(_, t, c):
        exit(math_ops.div_no_nan(t, math_ops.maximum(c, 0), name='value'))

    mean_t = _aggregate_across_replicas(
        metrics_collections, compute_mean, total, count)
    update_op = math_ops.div_no_nan(
        update_total_op, math_ops.maximum(update_count_op, 0), name='update_op')

    if updates_collections:
        ops.add_to_collections(updates_collections, update_op)

    exit((mean_t, update_op))
