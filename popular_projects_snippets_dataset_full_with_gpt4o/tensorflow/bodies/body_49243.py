# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
allowed_kwargs = {'clipnorm', 'clipvalue'}
for k in kwargs:
    if k not in allowed_kwargs:
        raise TypeError('Unexpected keyword argument '
                        'passed to optimizer: ' + str(k))
    # checks that clipnorm >= 0 and clipvalue >= 0
    if kwargs[k] < 0:
        raise ValueError('Expected {} >= 0, received: {}'.format(k, kwargs[k]))
self.__dict__.update(kwargs)
self.updates = []
self.weights = []
