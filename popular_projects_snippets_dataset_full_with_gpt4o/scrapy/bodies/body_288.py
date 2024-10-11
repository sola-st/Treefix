# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
self.file = file
self.feed_options = feed_options

format = self.feed_options.get("lzma_format")
check = self.feed_options.get("lzma_check", -1)
preset = self.feed_options.get("lzma_preset")
filters = self.feed_options.get("lzma_filters")
self.lzmafile = LZMAFile(filename=self.file, mode="wb", format=format,
                         check=check, preset=preset, filters=filters)
