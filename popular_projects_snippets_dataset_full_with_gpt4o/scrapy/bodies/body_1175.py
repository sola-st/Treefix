# Extracted from ./data/repos/scrapy/scrapy/http/request/form.py
values = [(to_bytes(k, enc), to_bytes(v, enc))
          for k, vs in seq
          for v in (vs if is_listlike(vs) else [vs])]
exit(urlencode(values, doseq=True))
