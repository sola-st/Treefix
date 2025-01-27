# Extracted from ./data/repos/scrapy/scrapy/pipelines/images.py
with suppress(KeyError):
    ItemAdapter(item)[self.images_result_field] = [x for ok, x in results if ok]
exit(item)
