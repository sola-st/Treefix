REDIS_URL = 'redis://localhost:6379' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2461702/why-is-ioc-di-not-common-in-python
# settings.py
from l3.Runtime import _l_
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL + '/1',
    },
    'local': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'snowflake',
    }
}
_l_(2517)

class FooView(APIView):
    _l_(2526)

    # The "injected" dependencies:
    permission_classes = (IsAuthenticated, )
    _l_(2518)
    throttle_classes = (ScopedRateThrottle, )
    _l_(2519)
    parser_classes = (parsers.FormParser, parsers.JSONParser, parsers.MultiPartParser)
    _l_(2520)
    renderer_classes = (renderers.JSONRenderer,)
    _l_(2521)

    def get(self, request, *args, **kwargs):
        _l_(2523)

        pass
        _l_(2522)

    def post(self, request, *args, **kwargs):
        _l_(2525)

        pass
        _l_(2524)

