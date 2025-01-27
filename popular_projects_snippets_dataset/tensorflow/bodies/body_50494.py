# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
logs = logs or {}
loss = logs.get('loss')
if loss is not None:
    loss = tf_utils.sync_to_numpy_or_python_type(loss)
    if np.isnan(loss) or np.isinf(loss):
        print('Batch %d: Invalid loss, terminating training' % (batch))
        self.model.stop_training = True
