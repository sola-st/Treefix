# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
for cell in cells:
    if not 'call' in dir(cell):
        raise ValueError('All cells must have a `call` method. '
                         'received cells:', cells)
    if not 'state_size' in dir(cell):
        raise ValueError('All cells must have a '
                         '`state_size` attribute. '
                         'received cells:', cells)
self.cells = cells
# reverse_state_order determines whether the state size will be in a reverse
# order of the cells' state. User might want to set this to True to keep the
# existing behavior. This is only useful when use RNN(return_state=True)
# since the state will be returned as the same order of state_size.
self.reverse_state_order = kwargs.pop('reverse_state_order', False)
if self.reverse_state_order:
    logging.warning('reverse_state_order=True in StackedRNNCells will soon '
                    'be deprecated. Please update the code to work with the '
                    'natural order of states if you rely on the RNN states, '
                    'eg RNN(return_state=True).')
super(StackedRNNCells, self).__init__(**kwargs)
