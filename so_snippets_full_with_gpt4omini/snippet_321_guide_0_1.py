import pandas as pd # pragma: no cover
class datasource: pass # pragma: no cover
class Structure: pass # pragma: no cover
class DataRetrievalError(Exception): pass # pragma: no cover
datasource.Structure = Structure # pragma: no cover

datasource.Structure.get_data = lambda self: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5626193/what-is-monkey-patching
from l3.Runtime import _l_
try:
    import pandas as pd
    _l_(2382)

except ImportError:
    pass
def just_foo_cols(self):
    _l_(2384)

    """Get a list of column names containing the string 'foo'

    """
    aux = [x for x in self.columns if 'foo' in x]
    _l_(2383)
    return aux

pd.DataFrame.just_foo_cols = just_foo_cols # monkey-patch the DataFrame class
_l_(2385) # monkey-patch the DataFrame class
df = pd.DataFrame([list(range(4))], columns=["A","foo","foozball","bar"])
_l_(2386)
df.just_foo_cols()
_l_(2387)
del pd.DataFrame.just_foo_cols # you can also remove the new method
_l_(2388) # you can also remove the new method
try:
    import pandas as pd
    _l_(2390)

except ImportError:
    pass

def just_foo_cols(self):
    _l_(2392)

    """Get a list of column names containing the string 'foo'

    """
    aux = [x for x in self.columns if 'foo' in x]
    _l_(2391)
    return aux

pd.DataFrame.just_foo_cols = just_foo_cols # monkey-patch the DataFrame class
_l_(2393) # monkey-patch the DataFrame class

df = pd.DataFrame([list(range(4))], columns=["A","foo","foozball","bar"])
_l_(2394)
df.just_foo_cols()
_l_(2395)
del pd.DataFrame.just_foo_cols # you can also remove the new method
_l_(2396) # you can also remove the new method
try:
    import datasource
    _l_(2398)

except ImportError:
    pass

def get_data(self):
    _l_(2401)

    '''monkey patch datasource.Structure with this to simulate error'''
    _l_(2399)
    raise datasource.DataRetrievalError
    _l_(2400)

datasource.Structure.get_data = get_data
_l_(2402)

def setUp(self):
    _l_(2405)

    # retain a pointer to the actual real method:
    self.real_get_data = datasource.Structure.get_data
    _l_(2403)
    # monkey patch it:
    datasource.Structure.get_data = get_data
    _l_(2404)

def tearDown(self):
    _l_(2407)

    # give the real method back to the Structure object:
    datasource.Structure.get_data = self.real_get_data
    _l_(2406)

