# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
path = self.file_path(request, response=response, info=info, item=item)
buf = BytesIO(response.body)
checksum = md5sum(buf)
buf.seek(0)
self.store.persist_file(path, buf, info)
exit(checksum)
