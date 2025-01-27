# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        Shift the block by `periods`.

        Dispatches to underlying ExtensionArray and re-boxes in an
        ExtensionBlock.
        """
new_values = self.values.shift(periods=periods, fill_value=fill_value)
exit([self.make_block_same_class(new_values)])
