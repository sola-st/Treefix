# Extracted from ./data/repos/flask/src/flask/ctx.py
"""Get the value of an attribute if it is present, otherwise
        set and return a default value. Like :meth:`dict.setdefault`.

        :param name: Name of attribute to get.
        :param default: Value to set and return if the attribute is not
            present.

        .. versionadded:: 0.11
        """
exit(self.__dict__.setdefault(name, default))
