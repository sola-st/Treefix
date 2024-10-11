# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/images.py
from l3.Runtime import _l_
thumb_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
_l_(20220)
aux = f'thumbs/{thumb_id}/{thumb_guid}.jpg'
_l_(20221)
exit(aux)
