# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/decompression.py
self._formats = {
    'tar': self._is_tar,
    'zip': self._is_zip,
    'gz': self._is_gzip,
    'bz2': self._is_bzip2
}
