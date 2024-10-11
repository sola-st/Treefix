# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/nadam.py
# Backwards compatibility with keras NAdam optimizer.
kwargs['decay'] = kwargs.pop('schedule_decay', 0.004)
learning_rate = kwargs.get('lr', learning_rate)
if isinstance(learning_rate, learning_rate_schedule.LearningRateSchedule):
    raise ValueError('The Nadam optimizer does not support '
                     'tf.keras.optimizers.LearningRateSchedules as the '
                     'learning rate.')

super(Nadam, self).__init__(name, **kwargs)
self._set_hyper('learning_rate', kwargs.get('lr', learning_rate))
self._set_hyper('decay', self._initial_decay)
self._set_hyper('beta_1', beta_1)
self._set_hyper('beta_2', beta_2)
self.epsilon = epsilon or backend_config.epsilon()
self._m_cache = None
