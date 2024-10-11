import json # pragma: no cover
import numpy as np # pragma: no cover

data = np.array([1, 2, 3, 4, 5]) # pragma: no cover
path = 'output.json' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
from l3.Runtime import _l_
try:
    import json
    _l_(2355)

except ImportError:
    pass
try:
    import numpy as np
    _l_(2357)

except ImportError:
    pass

class NumpyEncoder(json.JSONEncoder):
    _l_(2366)

    """ Special json encoder for numpy types """
    def default(self, obj):
        _l_(2365)

        if isinstance(obj, np.integer):
            _l_(2363)

            aux = int(obj)
            _l_(2358)
            return aux
        elif isinstance(obj, np.floating):
            _l_(2362)

            aux = float(obj)
            _l_(2359)
            return aux
        elif isinstance(obj, np.ndarray):
            _l_(2361)

            aux = obj.tolist()
            _l_(2360)
            return aux
        aux = json.JSONEncoder.default(self, obj)
        _l_(2364)
        return aux

dumped = json.dumps(data, cls=NumpyEncoder)
_l_(2367)

with open(path, 'w') as f:
    _l_(2369)

    json.dump(dumped, f)
    _l_(2368)

