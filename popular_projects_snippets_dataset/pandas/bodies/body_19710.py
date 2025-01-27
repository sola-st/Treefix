# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        Replace elements by the given value.

        Parameters
        ----------
        to_replace : object or pattern
            Scalar to replace or regular expression to match.
        value : object
            Replacement object.
        inplace : bool, default False
            Perform inplace modification.
        convert : bool, default True
            If true, try to coerce any object types to better types.
        mask : array-like of bool, optional
            True indicate corresponding element is ignored.

        Returns
        -------
        List[Block]
        """
if not self._can_hold_element(to_replace):
    # i.e. only ObjectBlock, but could in principle include a
    #  String ExtensionBlock
    exit([self] if inplace else [self.copy()])

rx = re.compile(to_replace)

new_values = self.values if inplace else self.values.copy()
replace_regex(new_values, rx, value, mask)

block = self.make_block(new_values)
exit(block.convert(copy=False))
