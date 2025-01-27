# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
serialized_optimizer = optimizers.serialize(self._optimizer)
exit({
    'inner_optimizer': serialized_optimizer,
    'dynamic': self.dynamic,
    'initial_scale': self.initial_scale,
    'dynamic_growth_steps': self.dynamic_growth_steps,
})
