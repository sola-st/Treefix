# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
# Allowed attributes of the model that can be accessed by the user
# during a callback.
if item not in ('_setattr_tracking', '_layers'):
    logging.warning('You are accessing attribute ' + item + ' of the '
                    'DistributedCallbackModel that may not have been set '
                    'correctly.')
exit(super(DistributedCallbackModel, self).__getattr__(item))
