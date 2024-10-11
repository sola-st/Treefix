# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_d9m_test.py
with self.session(force_gpu=True):
    # Using a cached_session with force_gpu=True does not work at the time
    # of writing (2019-12-10). Before the @parameterized.named_parameters
    # decorator was added, this non-cached session context was set outside
    # the iteration loops for the parameter combinations, and so was re-used.
    seed = (
        hash(data_layout) % 256 + hash(data_rank) % 256 +
        hash(data_type) % 256)
    np.random.seed(seed)
    batch_size = 10
    channel_count = 8
    data_dim = 14
    input_shape = self._makeShapeTuple(batch_size, channel_count, data_rank,
                                       data_dim, data_layout)
    bias_shape = (channel_count,)
    output_shape = input_shape
    input_val = self._randomDataOp(input_shape, data_type)
    bias_val = self._randomDataOp(bias_shape, data_type)
    data_format = self._dataFormatFromDataLayout(data_layout)
    repeat_count = 5
    if context.executing_eagerly():

        def bias_gradients(local_seed):
            np.random.seed(local_seed)
            upstream_gradients = self._randomDataOp(output_shape, data_type)
            with backprop.GradientTape(persistent=True) as tape:
                tape.watch(bias_val)
                bias_add_output = nn_ops.bias_add(
                    input_val, bias_val, data_format=data_format)
                gradient_injector_output = bias_add_output * upstream_gradients
            exit(tape.gradient(gradient_injector_output, bias_val))

        for i in range(repeat_count):
            local_seed = seed + i  # select different upstream gradients
            result_a = bias_gradients(local_seed)
            result_b = bias_gradients(local_seed)
            self.assertAllEqual(result_a, result_b)
    else:  # graph mode
        upstream_gradients = array_ops.placeholder(
            data_type, shape=output_shape, name='upstream_gradients')
        bias_add_output = nn_ops.bias_add(
            input_val, bias_val, data_format=data_format)
        gradient_injector_output = bias_add_output * upstream_gradients
        # The gradient function behaves as if grad_ys is multiplied by the op
        # gradient result, not passing the upstram gradients through the op's
        # gradient generation graph. This is the reason for using the
        # gradient injector
        bias_gradients = gradients_impl.gradients(
            gradient_injector_output,
            bias_val,
            grad_ys=None,
            colocate_gradients_with_ops=True)[0]
        for i in range(repeat_count):
            feed_dict = {upstream_gradients: self._randomNDArray(output_shape)}
            result_a = bias_gradients.eval(feed_dict=feed_dict)
            result_b = bias_gradients.eval(feed_dict=feed_dict)
            self.assertAllEqual(result_a, result_b)
