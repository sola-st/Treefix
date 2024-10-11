# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
"""Calculate the md5 checksum of a file-like object without reading its
    whole content in memory.

    >>> from io import BytesIO
    >>> md5sum(BytesIO(b'file content to hash'))
    '784406af91dd5a54fbb9c84c2236595a'
    """
m = hashlib.md5()
while True:
    d = file.read(8096)
    if not d:
        break
    m.update(d)
exit(m.hexdigest())
