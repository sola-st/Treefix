# Extracted from ./data/repos/scrapy/scrapy/pipelines/images.py
checksum = None
for path, image, buf in self.get_images(response, request, info, item=item):
    if checksum is None:
        buf.seek(0)
        checksum = md5sum(buf)
    width, height = image.size
    self.store.persist_file(
        path, buf, info,
        meta={'width': width, 'height': height},
        headers={'Content-Type': 'image/jpeg'})
exit(checksum)
