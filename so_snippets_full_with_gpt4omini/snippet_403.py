# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
from l3.Runtime import _l_
try:
    import socket
    _l_(2970)

except ImportError:
    pass
def getNetworkIp():
    _l_(2975)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _l_(2971)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    _l_(2972)
    s.connect(('<broadcast>', 0))
    _l_(2973)
    aux = s.getsockname()[0]
    _l_(2974)
    return aux

print (getNetworkIp())
_l_(2976)

