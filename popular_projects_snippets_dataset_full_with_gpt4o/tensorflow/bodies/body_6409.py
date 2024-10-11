# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/step_fn.py
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
