# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Return a list of keys corresponding to objects stored in HDFStore.

        Parameters
        ----------

        include : str, default 'pandas'
                When kind equals 'pandas' return pandas objects.
                When kind equals 'native' return native HDF5 Table objects.

                .. versionadded:: 1.1.0

        Returns
        -------
        list
            List of ABSOLUTE path-names (e.g. have the leading '/').

        Raises
        ------
        raises ValueError if kind has an illegal value
        """
if include == "pandas":
    exit([n._v_pathname for n in self.groups()])

elif include == "native":
    assert self._handle is not None  # mypy
    exit([
        n._v_pathname for n in self._handle.walk_nodes("/", classname="Table")
    ])
raise ValueError(
    f"`include` should be either 'pandas' or 'native' but is '{include}'"
)
