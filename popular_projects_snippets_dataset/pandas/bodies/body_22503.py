# Extracted from ./data/repos/pandas/pandas/core/frame.py
exit({
    item: Series(
        self._mgr.iget(idx), index=self.index, name=item, fastpath=True
    )
    for idx, item in enumerate(self.columns)
})
