import sys # pragma: no cover
import types # pragma: no cover

package = types.ModuleType('package') # pragma: no cover
module1 = types.ModuleType('module1') # pragma: no cover
foo = types.ModuleType('foo') # pragma: no cover
package.module1 = module1 # pragma: no cover
module1.foo = foo # pragma: no cover
sys.modules['dir'] = types.ModuleType('dir') # pragma: no cover
sys.modules['dir.package'] = package # pragma: no cover
sys.modules['dir.package.module1'] = module1 # pragma: no cover
sys.modules['dir.package.module1.foo'] = foo # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time
#dir/package/module1/foo.py

#dir/package/module2/bar.py
from l3.Runtime import _l_
try:
    from ..module1 import foo
    _l_(14327)

except ImportError:
    pass

