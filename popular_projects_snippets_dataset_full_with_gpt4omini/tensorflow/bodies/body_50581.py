# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
logs = logs or {}
logs['lr'] = backend.get_value(self.model.optimizer.lr)
current = logs.get(self.monitor)
if current is None:
    logging.warning('Learning rate reduction is conditioned on metric `%s` '
                    'which is not available. Available metrics are: %s',
                    self.monitor, ','.join(list(logs.keys())))

else:
    if self.in_cooldown():
        self.cooldown_counter -= 1
        self.wait = 0

    if self.monitor_op(current, self.best):
        self.best = current
        self.wait = 0
    elif not self.in_cooldown():
        self.wait += 1
        if self.wait >= self.patience:
            old_lr = backend.get_value(self.model.optimizer.lr)
            if old_lr > np.float32(self.min_lr):
                new_lr = old_lr * self.factor
                new_lr = max(new_lr, self.min_lr)
                backend.set_value(self.model.optimizer.lr, new_lr)
                if self.verbose > 0:
                    print('\nEpoch %05d: ReduceLROnPlateau reducing learning '
                          'rate to %s.' % (epoch + 1, new_lr))
                self.cooldown_counter = self.cooldown
                self.wait = 0
