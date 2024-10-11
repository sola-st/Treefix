from werkzeug.exceptions import Aborter # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.aborter_class = Aborter # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Create the object to assign to :attr:`aborter`. That object
        is called by :func:`flask.abort` to raise HTTP errors, and can
        be called directly as well.

        By default, this creates an instance of :attr:`aborter_class`,
        which defaults to :class:`werkzeug.exceptions.Aborter`.

        .. versionadded:: 2.2
        """
aux = self.aborter_class()
_l_(8056)
exit(aux)
