# Extracted from ./data/repos/scrapy/scrapy/pipelines/images.py
image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
exit(f'full/{image_guid}.jpg')
