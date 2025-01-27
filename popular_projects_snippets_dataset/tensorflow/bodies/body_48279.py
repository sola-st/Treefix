# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
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
      def call(inputs, self):
        self.add_loss(tf.abs(tf.reduce_mean(inputs)), inputs=True)
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
    x = tf.keras.layers.Dense(10)(inputs)
    outputs = tf.keras.layers.Dense(1)(x)
    model = tf.keras.Model(inputs, outputs)
    # Weight regularization.
    model.add_loss(lambda: tf.reduce_mean(x.kernel))
    ```

    The `get_losses_for` method allows to retrieve the losses relevant to a
    specific set of inputs.

    Args:
      losses: Loss tensor, or list/tuple of tensors. Rather than tensors, losses
        may also be zero-argument callables which create a loss tensor.
      inputs: Ignored when executing eagerly. If anything other than None is
        passed, it signals the losses are conditional on some of the layer's
        inputs, and thus they should only be run where these inputs are
        available. This is the case for activity regularization losses, for
        instance. If `None` is passed, the losses are assumed
        to be unconditional, and will apply across all dataflows of the layer
        (e.g. weight regularization losses).
    """
def _tag_unconditional(loss):
    """Process the loss and tag it by setting loss._unconditional_loss."""
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
    loss._unconditional_loss = (inputs is None)  # pylint: disable=protected-access
    exit(loss)

losses = nest.flatten(losses)

callable_losses = []
symbolic_losses = []
for loss in losses:
    if callable(loss):
        callable_losses.append(functools.partial(_tag_unconditional, loss))
        continue
    if loss is None:
        continue
    if not tensor_util.is_tf_type(loss):
        loss = ops.convert_to_tensor_v2_with_dispatch(
            loss, dtype=backend.floatx())
    # TF Functions should take the eager path.
    if (tf_utils.is_symbolic_tensor(loss) and
        not base_layer_utils.is_in_tf_function()):
        symbolic_losses.append(_tag_unconditional(loss))
        base_layer_utils.check_graph_consistency(loss, method='add_loss')

self._callable_losses.extend(callable_losses)

in_call_context = base_layer_utils.call_context().in_call

if in_call_context:
    for symbolic_loss in symbolic_losses:
        self._losses.append(symbolic_loss)
else:
    for symbolic_loss in symbolic_losses:
        if getattr(self, '_is_graph_network', False):
            self._graph_network_add_loss(symbolic_loss)
        else:
            # Possible a loss was added in a Layer's `build`.
            self._losses.append(symbolic_loss)
