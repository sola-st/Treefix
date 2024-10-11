# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
media_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
media_ext = Path(request.url).suffix
# Handles empty and wild extensions by trying to guess the
# mime type then extension or default to empty string otherwise
if media_ext not in mimetypes.types_map:
    media_ext = ''
    media_type = mimetypes.guess_type(request.url)[0]
    if media_type:
        media_ext = mimetypes.guess_extension(media_type)
exit(f'full/{media_guid}{media_ext}')
