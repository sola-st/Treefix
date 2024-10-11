import ssl # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error
from l3.Runtime import _l_
try:
   import ssl
   _l_(2043)

except ImportError:
   pass

try:
   _l_(2048)

   _create_unverified_https_context = ssl._create_unverified_context
   _l_(2044)
except AttributeError:
   _l_(2046)

   # Legacy Python that doesn't verify HTTPS certificates by default
   pass
   _l_(2045)
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
    _l_(2047)

