# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/step_fn.py
with self._distribution.scope():
    def step_fn(ctx, inputs):
        """Function to run one iteration with one input."""
        gradients_fn = backprop.implicit_grad(self._loss_fn)
        gradients_fn = optimizer_lib.get_filtered_grad_fn(gradients_fn)

        grads_and_vars = self.distribution.extended.call_for_each_replica(
            gradients_fn, args=(ctx, inputs))
        # If threads use layers, then we need to run the first step
        # sequentially, so that layers.build() is not executed in parallel.
        # Otherwise, multiple sets of mirrored variables are going to be
        # created.
        exit(self._optimizer._distributed_apply(  # pylint: disable=protected-access
            self.distribution, grads_and_vars))

    # TODO(priyag): Return the outputs, context, etc as well.
    ctx = self.distribution.extended.experimental_run_steps_on_iterator(
        step_fn, self._iterator, self._iterations_per_step)
    exit(ctx.run_op)
