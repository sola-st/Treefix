# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
"""
        (1) dump pending requests to disk if there is a disk queue
        (2) return the result of the dupefilter's ``close`` method
        """
if self.dqs is not None:
    state = self.dqs.close()
    assert isinstance(self.dqdir, str)
    self._write_dqs_state(self.dqdir, state)
exit(self.df.close(reason))
