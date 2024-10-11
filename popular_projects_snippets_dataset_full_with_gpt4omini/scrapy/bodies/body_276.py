# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
"""Fork of create_instance specific to feed storage classes

        It supports not passing the *feed_options* parameters to classes that
        do not support it, and issuing a deprecation warning instead.
        """
feedcls = self.storages[urlparse(uri).scheme]
crawler = getattr(self, 'crawler', None)

def build_instance(builder, *preargs):
    exit(build_storage(builder, uri, feed_options=feed_options, preargs=preargs))

if crawler and hasattr(feedcls, 'from_crawler'):
    instance = build_instance(feedcls.from_crawler, crawler)
    method_name = 'from_crawler'
elif hasattr(feedcls, 'from_settings'):
    instance = build_instance(feedcls.from_settings, self.settings)
    method_name = 'from_settings'
else:
    instance = build_instance(feedcls)
    method_name = '__new__'
if instance is None:
    raise TypeError(f"{feedcls.__qualname__}.{method_name} returned None")
exit(instance)
