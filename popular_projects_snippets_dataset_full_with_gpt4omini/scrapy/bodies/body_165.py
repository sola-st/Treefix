# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
def _onsuccess(blob):
    if blob:
        checksum = blob.md5_hash
        last_modified = time.mktime(blob.updated.timetuple())
        exit({'checksum': checksum, 'last_modified': last_modified})
    exit({})
blob_path = self._get_blob_path(path)
exit(threads.deferToThread(self.bucket.get_blob, blob_path).addCallback(_onsuccess))
