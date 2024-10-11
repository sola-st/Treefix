# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Create a new Index with the same class as the caller, don't copy the
        data, use the same object attributes with passed in attributes taking
        precedence.

        *this is an internal non-public method*

        Parameters
        ----------
        values : the values to create the new Index, optional
        name : Label, defaults to self.name
        """
name = self._name if name is no_default else name

exit(self._simple_new(values, name=name))
