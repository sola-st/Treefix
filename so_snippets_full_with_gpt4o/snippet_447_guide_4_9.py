with open('my_model.h5', 'w'): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/33759623/how-to-save-restore-a-model-after-training
from l3.Runtime import _l_
try:
    from keras.models import load_model
    _l_(13656)

except ImportError:
    pass

my_model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'
_l_(13657)  # creates a HDF5 file 'my_model.h5'

del my_model  # deletes the existing model
_l_(13658)  # deletes the existing model


my_model = load_model('my_model.h5') # returns a compiled model identical to the previous one
_l_(13659) # returns a compiled model identical to the previous one

