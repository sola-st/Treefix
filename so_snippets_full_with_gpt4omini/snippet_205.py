# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python

from l3.Runtime import _l_
try:
    import uuid
    _l_(989)

except ImportError:
    pass

def get_uuid_id():
    _l_(991)

    aux = str(uuid.uuid4())
    _l_(990)
    return aux

print(get_uuid_id()) 
_l_(992) 

