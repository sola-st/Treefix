# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Add loss tensor(s), potentially dependent on layer inputs.

    Some losses (for instance, activity regularization losses) may be dependent
    on the inputs passed when calling a layer. Hence, when reusing the same
    layer on different inputs `a` and `b`, some entries in `layer.losses` may
    be dependent on `a` and some on `b`. This method automatically keeps track
    of dependencies.

    This method can be used inside a subclassed layer or model's `call`
    function, in which case `losses` should be a Tensor or list of Tensors.

    Example:

    ```python
    class MyLayer(tf.keras.layers.Layer):
      def call(self, inputs):
        self.add_loss(tf.abs(tf.reduce_mean(inputs)))
        return inputs
    ```

    This method can also be called directly on a Functional Model during
    construction. In this case, any loss Tensors passed to this Model must
    be symbolic and be able to be traced back to the model's `Input`s. These
    losses become part of the model's topology and are tracked in `get_config`.

    Example:

    ```python
    inputs = tf.keras.Input(shape=(10,))
    x = tf.keras.layers.Dense(10)(inputs)
    outputs = tf.keras.layers.Dense(1)(x)
    model = tf.keras.Model(inputs, outputs)
    # Activity regularization.
    model.add_loss(tf.abs(tf.reduce_mean(x)))
    ```

    If this is not the case for your loss (if, for example, your loss references
    a `Variable` of one of the model's layers), you can wrap your loss in a
    zero-argument lambda. These losses are not tracked as part of the model's
    topology since they can't be serialized.

    Example:

    ```python
    inputs = tf.keras.Input(shape=(10,))
    d = tf.keras.layers.Dense(10)
    x = d(inputs)
    outputs = tf.keras.layers.Dense(1)(x)
    model = tf.keras.Model(inputs, outputs)
    # Weight regularization.
    model.add_loss(lambda: tf.reduce_mean(d.kernel))
    ```

    Args:
      losses: Loss tensor, or list/tuple of tensors. Rather than tensors, losses
        may also be zero-argument callables which create a loss tensor.
      **kwargs: Additional keyword arguments for backward compatibility.
        Accepted values:
          inputs - Deprecated, will be automatically inferred.
    """
kwargs.pop('inputs', None)
if kwargs:
    raise TypeError('Unknown keyword arguments: %s' % (kwargs.keys(),))

def _tag_callable(loss):
    """Tags callable loss tensor as `_unconditional_loss`."""
    if callable(loss):
        # We run the loss without autocasting, as regularizers are often
        # numerically unstable in float16.
        with autocast_variable.enable_auto_cast_variables(None):
            loss = loss()
    if loss is None:
        exit(None)  # Will be filtered out when computing the .losses property
    if not tensor_util.is_tf_type(loss):
        loss = ops.convert_to_tensor_v2_with_dispatch(
            loss, dtype=backend.floatx())
    loss._unconditional_loss = True  # pylint: disable=protected-access
    exit(loss)

losses = nest.flatten(losses)

callable_losses = []
eager_losses = []
symbolic_losses = []
for loss in losses:
    if callable(loss):
        callable_losses.append(functools.partial(_tag_callable, loss))
        continue
    if loss is None:
        continue
    if not tensor_util.is_tf_type(loss) and not isinstance(
        loss, keras_tensor.KerasTensor):
        loss = ops.convert_to_tensor_v2_with_dispatch(
            loss, dtype=backend.floatx())
    # TF Functions should take the eager path.
    if ((tf_utils.is_symbolic_tensor(loss) or
         isinstance(loss, keras_tensor.KerasTensor)) and
        not base_layer_utils.is_in_tf_function()):
        symbolic_losses.append(loss)
    elif tensor_util.is_tf_type(loss):
        eager_losses.append(loss)

self._callable_losses.extend(callable_losses)

in_call_context = base_layer_utils.call_context().in_call
if eager_losses and not in_call_context:
    raise ValueError(
        'Expected a symbolic Tensors or a callable for the loss value. '
        'Please wrap your loss computation in a zero argument `lambda`.')

self._eager_losses.extend(eager_losses)

for symbolic_loss in symbolic_losses:
    if getattr(self, '_is_graph_network', False):
        self._graph_network_add_loss(symbolic_loss)
    else:
        # Possible a loss was added in a Layer's `build`.
        self._losses.append(symbolic_loss)
