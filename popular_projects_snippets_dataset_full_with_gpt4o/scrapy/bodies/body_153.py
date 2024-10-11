# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
absolute_path = self._get_filesystem_path(path)
self._mkdir(absolute_path.parent, info)
absolute_path.write_bytes(buf.getvalue())
