# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
self.file = file
self.feed_options = feed_options
compress_level = self.feed_options.get("gzip_compresslevel", 9)
mtime = self.feed_options.get("gzip_mtime")
filename = self.feed_options.get("gzip_filename")
self.gzipfile = GzipFile(fileobj=self.file, mode="wb", compresslevel=compress_level,
                         mtime=mtime, filename=filename)
