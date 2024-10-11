import json # pragma: no cover
import numpy as np # pragma: no cover

data = np.array([1.1, 2.2, 3.3]) # pragma: no cover
path = 'output.json' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
from l3.Runtime import _l_
try:
    import json
    _l_(14700)

except ImportError:
    pass
try:
    import numpy as np
    _l_(14702)

except ImportError:
    pass

class NumpyEncoder(json.JSONEncoder):
    _l_(14711)

    """ Special json encoder for numpy types """
    def default(self, obj):
        _l_(14710)

        if isinstance(obj, np.integer):
            _l_(14708)

            aux = int(obj)
            _l_(14703)
            return aux
        elif isinstance(obj, np.floating):
            _l_(14707)

            aux = float(obj)
            _l_(14704)
            return aux
        elif isinstance(obj, np.ndarray):
            _l_(14706)

            aux = obj.tolist()
            _l_(14705)
            return aux
        aux = json.JSONEncoder.default(self, obj)
        _l_(14709)
        return aux

dumped = json.dumps(data, cls=NumpyEncoder)
_l_(14712)

with open(path, 'w') as f:
    _l_(14714)

    json.dump(dumped, f)
    _l_(14713)

