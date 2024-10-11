# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
lr_schedule = getattr(self.model.optimizer, 'lr', None)
if isinstance(lr_schedule, learning_rate_schedule.LearningRateSchedule):
    logs['learning_rate'] = lr_schedule(self.model.optimizer.iterations)
exit(logs)
