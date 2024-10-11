import pandas as pd # pragma: no cover
import types # pragma: no cover

class DataRetrievalError(Exception): pass # pragma: no cover
datasource = types.ModuleType('datasource') # pragma: no cover
datasource.DataRetrievalError = DataRetrievalError # pragma: no cover
class Structure: # pragma: no cover
    def get_data(self): pass # pragma: no cover
datasource.Structure = Structure() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5626193/what-is-monkey-patching
from l3.Runtime import _l_
try:
    import pandas as pd
    _l_(14034)

except ImportError:
    pass
def just_foo_cols(self):
    _l_(14036)

    """Get a list of column names containing the string 'foo'

    """
    aux = [x for x in self.columns if 'foo' in x]
    _l_(14035)
    return aux

pd.DataFrame.just_foo_cols = just_foo_cols # monkey-patch the DataFrame class
_l_(14037) # monkey-patch the DataFrame class
df = pd.DataFrame([list(range(4))], columns=["A","foo","foozball","bar"])
_l_(14038)
df.just_foo_cols()
_l_(14039)
del pd.DataFrame.just_foo_cols # you can also remove the new method
_l_(14040) # you can also remove the new method
try:
    import pandas as pd
    _l_(14042)

except ImportError:
    pass

def just_foo_cols(self):
    _l_(14044)

    """Get a list of column names containing the string 'foo'

    """
    aux = [x for x in self.columns if 'foo' in x]
    _l_(14043)
    return aux

pd.DataFrame.just_foo_cols = just_foo_cols # monkey-patch the DataFrame class
_l_(14045) # monkey-patch the DataFrame class

df = pd.DataFrame([list(range(4))], columns=["A","foo","foozball","bar"])
_l_(14046)
df.just_foo_cols()
_l_(14047)
del pd.DataFrame.just_foo_cols # you can also remove the new method
_l_(14048) # you can also remove the new method
try:
    import datasource
    _l_(14050)

except ImportError:
    pass

def get_data(self):
    _l_(14053)

    '''monkey patch datasource.Structure with this to simulate error'''
    _l_(14051)
    raise datasource.DataRetrievalError
    _l_(14052)

datasource.Structure.get_data = get_data
_l_(14054)

def setUp(self):
    _l_(14057)

    # retain a pointer to the actual real method:
    self.real_get_data = datasource.Structure.get_data
    _l_(14055)
    # monkey patch it:
    datasource.Structure.get_data = get_data
    _l_(14056)

def tearDown(self):
    _l_(14059)

    # give the real method back to the Structure object:
    datasource.Structure.get_data = self.real_get_data
    _l_(14058)

