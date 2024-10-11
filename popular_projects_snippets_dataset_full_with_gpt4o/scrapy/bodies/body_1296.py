# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/decompression.py
archive = BytesIO(response.body)
try:
    zip_file = zipfile.ZipFile(archive)
except zipfile.BadZipfile:
    exit()

namelist = zip_file.namelist()
body = zip_file.read(namelist[0])
respcls = responsetypes.from_args(filename=namelist[0], body=body)
exit(response.replace(body=body, cls=respcls))
