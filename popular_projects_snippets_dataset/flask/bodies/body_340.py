# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Alternative error attach function to the :meth:`errorhandler`
        decorator that is more straightforward to use for non decorator
        usage.

        .. versionadded:: 0.7
        """
exc_class, code = self._get_exc_class_and_code(code_or_exception)
_l_(16237)
self.error_handler_spec[None][code][exc_class] = f
_l_(16238)
