# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/ftp.py
message = result.getErrorMessage()
if result.type == CommandFailed:
    m = _CODE_RE.search(message)
    if m:
        ftpcode = m.group()
        httpcode = self.CODE_MAPPING.get(ftpcode, self.CODE_MAPPING["default"])
        exit(Response(url=request.url, status=httpcode, body=to_bytes(message)))
raise result.type(result.value)
