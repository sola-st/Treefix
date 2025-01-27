# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Checks that tensors passed to `add_*` method match the Keras graph.

  When one of the `add_*` method is called inside a V2 conditional branch,
  the underlying tensor gets created in a FuncGraph managed by control_flow_v2.
  We need to raise clear error messages in such cases.

  Args:
    tensor: Tensor to check, or `False` if it is known that an error
      should be raised.
    method: Caller method, one of {'add_metric', 'add_loss', 'add_update'}.
    force_raise: If an error should be raised regardless of `tensor`.

  Raises:
    RuntimeError: In case of an out-of-graph tensor.
  """
if (force_raise or
    (ops.executing_eagerly_outside_functions() and
     hasattr(tensor, 'graph') and tensor.graph.is_control_flow_graph)):
    if method == 'activity_regularizer':
        bad_example = """
      class TestModel(tf.keras.Model):

        def __init__(self):
          super(TestModel, self).__init__(name='test_model')
          self.dense = tf.keras.layers.Dense(2, activity_regularizer='l2')

        def call(self, x, training=None):
          if training:
            return self.dense(x)
          else:
            return self.dense(x)
      """
        correct_example = """
      class TestModel(tf.keras.Model):

        def __init__(self):
          super(TestModel, self).__init__(name='test_model')
          self.dense = tf.keras.layers.Dense(2, activity_regularizer='l2')

        def call(self, x, training=None):
          return self.dense(x)
      """
        raise RuntimeError(
            'You are using a layer with `activity_regularizer` in a control flow '
            'branch, e.g.:\n{bad_example}\nThis is currently not supported. '
            'Please move your call to the layer with `activity_regularizer` out '
            'of the control flow branch, e.g.:\n{correct_example}\n'
            'You can also resolve this by marking your outer model/layer dynamic'
            ' (eager-only) by passing `dynamic=True` to the layer constructor. '
            'Any kind of control flow is supported with dynamic layers. '
            'Note that using `dynamic=True` requires you to implement static '
            'shape inference in the `compute_output_shape(input_shape)` '
            'method.'.format(
                bad_example=bad_example, correct_example=correct_example))

    if method == 'add_metric':
        bad_example = """
      def call(self, inputs, training=None):
        if training:
          metric = compute_metric(inputs)
          self.add_metric(metric, name='my_metric', aggregation='mean')
        return inputs
      """
        correct_example = """
      def call(self, inputs, training=None):
        if training:
          metric = compute_metric(inputs)
        else:
          metric = 0.
        self.add_metric(metric, name='my_metric', aggregation='mean')
        return inputs
      """
    elif method == 'add_loss':
        bad_example = """
      def call(self, inputs, training=None):
        if training:
          loss = compute_loss(inputs)
          self.add_loss(loss)
        return inputs
      """
        correct_example = """
      def call(self, inputs, training=None):
        if training:
          loss = compute_loss(inputs)
        else:
          loss = 0.
        self.add_loss(loss)
        return inputs
      """
    else:
        bad_example = """
      def call(self, inputs, training=None):
        if training:
          self.add_update(self.w.assign_add(1))
        return inputs
      """
        correct_example = """
      def call(self, inputs, training=None):
        if training:
          increment = 1
        else:
          increment = 0
        self.add_update(self.w.assign_add(increment))
        return inputs
      """
    raise RuntimeError(
        'You are using the method `{method}` in a control flow branch '
        'in your layer, e.g.:\n{bad_example}\n'
        'This is not currently supported. '
        'Please move your call to {method} out of the control flow branch, '
        'e.g.:\n{correct_example}\n'
        'You can also resolve this by marking your layer '
        'as dynamic (eager-only) by passing '
        '`dynamic=True` to the layer constructor. '
        'Any kind of control flow is supported with dynamic layers. '
        'Note that using `dynamic=True` requires you '
        'to implement static shape inference '
        'in the `compute_output_shape(input_shape)` method.'.format(
            method=method,
            bad_example=bad_example,
            correct_example=correct_example))
