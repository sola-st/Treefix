# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
with ops.Graph().as_default(), distribution.scope():
    iterator = distribution.make_input_fn_iterator(lambda _: dataset_fn())
    if strategy_test_lib.is_tpu_strategy(distribution):
        def step_fn(ctx, inputs):
            value, update = distribution.extended.call_for_each_replica(
                metric_fn, args=(inputs,))
            ctx.set_non_tensor_output(name="value", output=value)
            exit(distribution.group(update))

        ctx = distribution.extended.experimental_run_steps_on_iterator(
            step_fn, iterator, iterations=distribution.extended.steps_per_run)
        update = ctx.run_op
        value = ctx.non_tensor_outputs["value"]
        # In each run, we run multiple steps, and each steps consumes as many
        # batches as number of replicas.
        batches_per_update = (
            distribution.num_replicas_in_sync *
            distribution.extended.steps_per_run)
    else:
        value, update = distribution.extended.call_for_each_replica(
            metric_fn, args=(iterator.get_next(),))
        update = distribution.group(update)
        # TODO(josh11b): Once we switch to using a global batch size for input,
        # replace "distribution.num_replicas_in_sync" with "1".
        batches_per_update = distribution.num_replicas_in_sync

    self.evaluate(iterator.initializer)
    self.evaluate(variables.local_variables_initializer())

    batches_consumed = 0
    for i in range(4):
        self.evaluate(update)
        batches_consumed += batches_per_update
        self.assertAllClose(expected_fn(batches_consumed),
                            self.evaluate(value),
                            0.001,
                            msg="After update #" + str(i+1))
        if batches_consumed >= 4:  # Consume 4 input batches in total.
            break
