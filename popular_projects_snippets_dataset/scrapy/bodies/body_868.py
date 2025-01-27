# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http2.py
if timeout_cl.active():
    timeout_cl.cancel()
    exit(response)

url = urldefrag(request.url)[0]
raise TimeoutError(f"Getting {url} took longer than {timeout} seconds.")
