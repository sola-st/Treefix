# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
absolute_path = self._get_filesystem_path(path)
try:
    last_modified = absolute_path.stat().st_mtime
except os.error:
    exit({})

with absolute_path.open('rb') as f:
    checksum = md5sum(f)

exit({'last_modified': last_modified, 'checksum': checksum})
