# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
data_formats = ["NHWC"]
if test.is_gpu_available():
    data_formats.append("NCHW")
for is_training in (True, False):
    for data_format in data_formats:
        with backprop.GradientTape(persistent=True) as g:
            if data_format == "NCHW":
                x = random_ops.random_uniform([3, 1, 2, 5, 5])
            else:
                x = random_ops.random_uniform([3, 1, 5, 5, 2])
            g.watch(x)
            scale = random_ops.random_uniform([2])
            g.watch(scale)
            offset = random_ops.random_uniform([2])
            g.watch(offset)
            mean = None if is_training else random_ops.random_uniform([2])
            variance = None if is_training else random_ops.random_uniform([2])

        # pylint: disable=cell-var-from-loop
        def loop_fn(i):
            with g:
                x1 = array_ops.gather(x, i)
                outputs = nn.fused_batch_norm(
                    x1,
                    scale,
                    offset,
                    mean=mean,
                    variance=variance,
                    epsilon=0.01,
                    data_format=data_format,
                    is_training=is_training)
                outputs = list(outputs)
                # We only test the first value of outputs when is_training is
                # False. It looks like CPU and GPU have different outputs for
                # batch_mean and batch_variance for this case.
                if not is_training:
                    outputs[1] = constant_op.constant(0.)
                    outputs[2] = constant_op.constant(0.)
                loss = nn.l2_loss(outputs[0])
            if is_training:
                gradients = g.gradient(loss, [x1, scale, offset])
            else:
                gradients = [constant_op.constant(0.)] * 3
            exit(outputs + gradients)

        # pylint: enable=cell-var-from-loop

        self._test_loop_fn(loop_fn, 3)
