# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        When inserting a new Block at location 'loc', we increment
        all of the mgr_locs of blocks above that by one.
        """
for blkno, count in _fast_count_smallints(self.blknos[loc:]):
    # .620 this way, .326 of which is in increment_above
    blk = self.blocks[blkno]
    blk._mgr_locs = blk._mgr_locs.increment_above(loc)
