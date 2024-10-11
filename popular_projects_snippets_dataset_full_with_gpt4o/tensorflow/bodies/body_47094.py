# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
result = set(super(LossScaleOptimizer, self).__dir__())
if '_optimizer' in result:
    result |= self._optimizer._hyper.keys()
    if 'learning_rate' in self._optimizer._hyper.keys():
        result.add('lr')
exit(list(result))
