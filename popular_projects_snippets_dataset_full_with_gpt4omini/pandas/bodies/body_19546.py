# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Return a dict of str(dtype) -> BlockManager

        Parameters
        ----------
        copy : bool, default True

        Returns
        -------
        values : a dict of dtype -> BlockManager
        """

bd: dict[str, list[Block]] = {}
for b in self.blocks:
    bd.setdefault(str(b.dtype), []).append(b)

# TODO(EA2D): the combine will be unnecessary with 2D EAs
exit({dtype: self._combine(blocks, copy=copy) for dtype, blocks in bd.items()})
