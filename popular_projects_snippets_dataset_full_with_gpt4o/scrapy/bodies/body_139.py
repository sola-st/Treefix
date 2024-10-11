# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
"""Make overridable methods of MediaPipeline and subclasses backwards compatible"""
methods = [
    "file_path", "thumb_path", "media_to_download", "media_downloaded",
    "file_downloaded", "image_downloaded", "get_images"
]

for method_name in methods:
    method = getattr(self, method_name, None)
    if callable(method):
        setattr(self, method_name, self._compatible(method))
