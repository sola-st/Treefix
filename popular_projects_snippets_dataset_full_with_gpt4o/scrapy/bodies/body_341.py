# Extracted from ./data/repos/scrapy/scrapy/responsetypes.py
self.classes = {}
self.mimetypes = MimeTypes()
mimedata = get_data('scrapy', 'mime.types').decode('utf8')
self.mimetypes.readfp(StringIO(mimedata))
for mimetype, cls in self.CLASSES.items():
    self.classes[mimetype] = load_object(cls)
