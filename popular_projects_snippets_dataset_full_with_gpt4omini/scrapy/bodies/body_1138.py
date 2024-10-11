# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
seq = seq.items() if isinstance(seq, Mapping) else seq
iseq = {}
for k, v in seq:
    iseq.setdefault(self.normkey(k), []).extend(self.normvalue(v))
super().update(iseq)
