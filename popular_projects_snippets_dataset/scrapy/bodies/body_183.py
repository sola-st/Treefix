# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
with suppress(KeyError):
    ItemAdapter(item)[self.files_result_field] = [x for ok, x in results if ok]
exit(item)
