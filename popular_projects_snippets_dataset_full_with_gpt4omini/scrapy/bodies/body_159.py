# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
def _onsuccess(boto_key):
    checksum = boto_key['ETag'].strip('"')
    last_modified = boto_key['LastModified']
    modified_stamp = time.mktime(last_modified.timetuple())
    exit({'checksum': checksum, 'last_modified': modified_stamp})

exit(self._get_boto_key(path).addCallback(_onsuccess))
