# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
super(ModelCheckpoint, self).__init__()
self._supports_tf_logs = True
self.monitor = monitor
self.verbose = verbose
self.filepath = path_to_string(filepath)
self.save_best_only = save_best_only
self.save_weights_only = save_weights_only
self.save_freq = save_freq
self.epochs_since_last_save = 0
self._batches_seen_since_last_saving = 0
self._last_batch_seen = 0

if save_weights_only:
    if options is None or isinstance(
        options, checkpoint_options_lib.CheckpointOptions):
        self._options = options or checkpoint_options_lib.CheckpointOptions()
    else:
        raise TypeError('If save_weights_only is True, then `options` must be '
                        'either None or a tf.train.CheckpointOptions')
else:
    if options is None or isinstance(options, save_options_lib.SaveOptions):
        self._options = options or save_options_lib.SaveOptions()
    else:
        raise TypeError('If save_weights_only is False, then `options` must be'
                        'either None or a tf.saved_model.SaveOptions')

    # Deprecated field `load_weights_on_restart` is for loading the checkpoint
    # file from `filepath` at the start of `model.fit()`
    # TODO(rchao): Remove the arg during next breaking release.
if 'load_weights_on_restart' in kwargs:
    self.load_weights_on_restart = kwargs['load_weights_on_restart']
    logging.warning('`load_weights_on_restart` argument is deprecated. '
                    'Please use `model.load_weights()` for loading weights '
                    'before the start of `model.fit()`.')
else:
    self.load_weights_on_restart = False

# Deprecated field `period` is for the number of epochs between which
# the model is saved.
if 'period' in kwargs:
    self.period = kwargs['period']
    logging.warning('`period` argument is deprecated. Please use `save_freq` '
                    'to specify the frequency in number of batches seen.')
else:
    self.period = 1

if mode not in ['auto', 'min', 'max']:
    logging.warning('ModelCheckpoint mode %s is unknown, '
                    'fallback to auto mode.', mode)
    mode = 'auto'

if mode == 'min':
    self.monitor_op = np.less
    self.best = np.Inf
elif mode == 'max':
    self.monitor_op = np.greater
    self.best = -np.Inf
else:
    if 'acc' in self.monitor or self.monitor.startswith('fmeasure'):
        self.monitor_op = np.greater
        self.best = -np.Inf
    else:
        self.monitor_op = np.less
        self.best = np.Inf

if self.save_freq != 'epoch' and not isinstance(self.save_freq, int):
    raise ValueError('Unrecognized save_freq: {}'.format(self.save_freq))

# Only the chief worker writes model checkpoints, but all workers
# restore checkpoint at on_train_begin().
self._chief_worker_only = False
