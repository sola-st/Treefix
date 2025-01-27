# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Retrieve pandas object stored in file.

        Parameters
        ----------
        key : str

        Returns
        -------
        object
            Same type as object stored in file.
        """
with patch_pickle():
    # GH#31167 Without this patch, pickle doesn't know how to unpickle
    #  old DateOffset objects now that they are cdef classes.
    group = self.get_node(key)
    if group is None:
        raise KeyError(f"No object named {key} in the file")
    exit(self._read_group(group))
