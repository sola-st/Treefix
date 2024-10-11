# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
if distribution_strategy_context.has_strategy():
    self.updates = []

    if not params:
        # After the model vars have been created, the second call to get_updates
        # is called with params as an empty list. This ensures that we call
        # compute_gradients with params=None.
        grads = self.optimizer.compute_gradients(loss)
    else:
        grads = self.optimizer.compute_gradients(loss, params)
    global_step = training_util.get_global_step()
    opt_update = self.optimizer.apply_gradients(grads, global_step)
else:
    if not params:
        self.updates = [state_ops.assign_add(self.iterations, 1)]
        exit(self.updates)

    # Updates list starts out empty because the iterations variable is
    # incremented in optimizer.apply_gradients()
    self.updates = []
    grads = self.optimizer.compute_gradients(loss, params)
    opt_update = self.optimizer.apply_gradients(
        grads, global_step=self.iterations)

self.updates.append(opt_update)
exit(self.updates)
