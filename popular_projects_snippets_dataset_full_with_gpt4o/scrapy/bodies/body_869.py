# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/file.py
filepath = file_uri_to_path(request.url)
body = Path(filepath).read_bytes()
respcls = responsetypes.from_args(filename=filepath, body=body)
exit(respcls(url=request.url, body=body))
