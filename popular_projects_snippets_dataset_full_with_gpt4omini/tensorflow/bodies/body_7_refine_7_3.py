tf = type('MockTF', (object,), { # pragma: no cover
    'compat': type('MockCompat', (object,), { # pragma: no cover
        'v2': type('MockV2', (object,), { # pragma: no cover
            'compat': type('MockCompatV1', (object,), { # pragma: no cover
                'v1': type('MockV1', (object,), {'keras': 'keras'}) # pragma: no cover
            })() # pragma: no cover
        })() # pragma: no cover
    })() # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/module_test.py
# pylint: disable=pointless-statement
from l3.Runtime import _l_
tf.compat.v2.compat.v1.keras
_l_(4966)
