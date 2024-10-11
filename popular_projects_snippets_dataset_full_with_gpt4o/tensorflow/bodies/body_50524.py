# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Saves the model.

    Args:
        epoch: the epoch this iteration is in.
        logs: the `logs` dict passed in to `on_batch_end` or `on_epoch_end`.
    """
logs = logs or {}

if isinstance(self.save_freq,
              int) or self.epochs_since_last_save >= self.period:
    # Block only when saving interval is reached.
    logs = tf_utils.sync_to_numpy_or_python_type(logs)
    self.epochs_since_last_save = 0
    filepath = self._get_file_path(epoch, logs)

    try:
        if self.save_best_only:
            current = logs.get(self.monitor)
            if current is None:
                logging.warning('Can save best model only with %s available, '
                                'skipping.', self.monitor)
            else:
                if self.monitor_op(current, self.best):
                    if self.verbose > 0:
                        print('\nEpoch %05d: %s improved from %0.5f to %0.5f,'
                              ' saving model to %s' % (epoch + 1, self.monitor,
                                                       self.best, current, filepath))
                    self.best = current
                    if self.save_weights_only:
                        self.model.save_weights(
                            filepath, overwrite=True, options=self._options)
                    else:
                        self.model.save(filepath, overwrite=True, options=self._options)
                else:
                    if self.verbose > 0:
                        print('\nEpoch %05d: %s did not improve from %0.5f' %
                              (epoch + 1, self.monitor, self.best))
        else:
            if self.verbose > 0:
                print('\nEpoch %05d: saving model to %s' % (epoch + 1, filepath))
            if self.save_weights_only:
                self.model.save_weights(
                    filepath, overwrite=True, options=self._options)
            else:
                self.model.save(filepath, overwrite=True, options=self._options)

        self._maybe_remove_file()
    except IsADirectoryError as e:  # h5py 3.x
        raise IOError('Please specify a non-directory filepath for '
                      'ModelCheckpoint. Filepath used is an existing '
                      'directory: {}'.format(filepath))
    except IOError as e:  # h5py 2.x
        # `e.errno` appears to be `None` so checking the content of `e.args[0]`.
        if 'is a directory' in str(e.args[0]).lower():
            raise IOError('Please specify a non-directory filepath for '
                          'ModelCheckpoint. Filepath used is an existing '
                          'directory: {}'.format(filepath))
        # Re-throw the error for any other causes.
        raise e
