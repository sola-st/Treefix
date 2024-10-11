# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/decompression.py
archive = BytesIO(response.body)
try:
    tar_file = tarfile.open(name=mktemp(), fileobj=archive)
except tarfile.ReadError:
    exit()

body = tar_file.extractfile(tar_file.members[0]).read()
respcls = responsetypes.from_args(filename=tar_file.members[0].name, body=body)
exit(response.replace(body=body, cls=respcls))
