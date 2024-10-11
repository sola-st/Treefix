class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.__dict__ = {'attribute1': 'value1', 'attribute2': 'value2'} # pragma: no cover
name = 'attribute1' # pragma: no cover
default = 'default_value' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
"""Get an attribute by name, or a default value. Like
        :meth:`dict.get`.

        :param name: Name of attribute to get.
        :param default: Value to return if the attribute is not present.

        .. versionadded:: 0.10
        """
aux = self.__dict__.get(name, default)
_l_(8638)
exit(aux)
