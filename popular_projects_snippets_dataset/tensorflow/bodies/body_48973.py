# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Check input assumptions set before layer building, e.g. input rank.
if not self.built:
    input_spec.assert_input_compatibility(
        self.input_spec, inputs, self.name)
    input_list = nest.flatten(inputs)
    if input_list and self._dtype_policy.compute_dtype is None:
        try:
            dtype = input_list[0].dtype.base_dtype.name
        except AttributeError:
            pass
        else:
            self._set_dtype_policy(policy.Policy(dtype))
    input_shapes = None
    # Converts Tensors / CompositeTensors to TensorShapes.
    if all(hasattr(x, 'shape') for x in input_list):
        input_shapes = tf_utils.get_shapes(inputs)
    else:
        # Converts input shape to TensorShapes.
        try:
            input_shapes = tf_utils.convert_shapes(inputs, to_tuples=False)
        except ValueError:
            pass
      # Only call `build` if the user has manually overridden the build method.
    if not hasattr(self.build, '_is_default'):
        # Any setup work performed only once should happen in an `init_scope`
        # to avoid creating symbolic Tensors that will later pollute any eager
        # operations.
        with tf_utils.maybe_init_scope(self):
            self.build(input_shapes)  # pylint:disable=not-callable
      # We must set also ensure that the layer is marked as built, and the build
      # shape is stored since user defined build functions may not be calling
      # `super.build()`
    Layer.build(self, input_shapes)

# Optionally load weight values specified at layer instantiation.
if self._initial_weights is not None:
    with ops.init_scope():
        # Using `init_scope` since we want variable assignment in
        # `set_weights` to be treated like variable initialization.
        self.set_weights(self._initial_weights)
    self._initial_weights = None
