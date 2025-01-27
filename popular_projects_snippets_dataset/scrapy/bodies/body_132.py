# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
self.download_func = download_func
self._expects_item = {}

if isinstance(settings, dict) or settings is None:
    settings = Settings(settings)
resolve = functools.partial(self._key_for_pipe,
                            base_class_name="MediaPipeline",
                            settings=settings)
self.allow_redirects = settings.getbool(
    resolve('MEDIA_ALLOW_REDIRECTS'), False
)
self._handle_statuses(self.allow_redirects)

# Check if deprecated methods are being used and make them compatible
self._make_compatible()
