import os # pragma: no cover
from jinja2.loaders import FileSystemLoader # pragma: no cover

self = type("MockSelf", (object,), { "template_folder": 'templates', "root_path": '/path/to/root' })() # pragma: no cover

import os # pragma: no cover
from jinja2 import FileSystemLoader # pragma: no cover

self = type('Mock', (object,), {'template_folder': 'templates', 'root_path': '/path/to/root'})() # pragma: no cover
os.path = type('Mock', (object,), {'join': lambda *args: '/'.join(args)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""The Jinja loader for this object's templates. By default this
        is a class :class:`jinja2.loaders.FileSystemLoader` to
        :attr:`template_folder` if it is set.

        .. versionadded:: 0.5
        """
if self.template_folder is not None:
    _l_(15662)

    aux = FileSystemLoader(os.path.join(self.root_path, self.template_folder))
    _l_(15660)
    exit(aux)
else:
    aux = None
    _l_(15661)
    exit(aux)
