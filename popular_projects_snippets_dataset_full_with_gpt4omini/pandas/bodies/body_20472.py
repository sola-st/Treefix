# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Optimized equivalent to `self.get_level_values(0).get_indexer_for(target)`.
        """
lev = self.levels[0]
codes = self._codes[0]
cat = Categorical.from_codes(codes=codes, categories=lev)
ci = Index(cat)
exit(ci.get_indexer_for(target))
