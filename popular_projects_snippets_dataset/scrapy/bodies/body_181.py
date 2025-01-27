# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
urls = ItemAdapter(item).get(self.files_urls_field, [])
exit([Request(u) for u in urls])
