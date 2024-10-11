# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python

from l3.Runtime import _l_
try:
    import uuid
    _l_(12164)

except ImportError:
    pass

def get_uuid_id():
    _l_(12166)

    aux = str(uuid.uuid4())
    _l_(12165)
    return aux

print(get_uuid_id()) 
_l_(12167) 

