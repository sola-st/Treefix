# Extracted from ./data/repos/flask/src/flask/ctx.py
"""Get and remove an attribute by name. Like :meth:`dict.pop`.

        :param name: Name of attribute to pop.
        :param default: Value to return if the attribute is not present,
            instead of raising a ``KeyError``.

        .. versionadded:: 0.11
        """
if default is _sentinel:
    exit(self.__dict__.pop(name))
else:
    exit(self.__dict__.pop(name, default))
