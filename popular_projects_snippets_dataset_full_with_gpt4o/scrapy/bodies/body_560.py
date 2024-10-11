# Extracted from ./data/repos/scrapy/scrapy/utils/datatypes.py
seq = seq.items() if isinstance(seq, Mapping) else seq
iseq = ((self.normkey(k), self.normvalue(v)) for k, v in seq)
super().update(iseq)
