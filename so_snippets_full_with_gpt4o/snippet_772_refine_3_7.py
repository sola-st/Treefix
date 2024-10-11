REDIS_URL = 'redis://127.0.0.1:6379' # pragma: no cover

REDIS_URL = 'redis://localhost:6379' # pragma: no cover
APIView = type('MockAPIView', (object,), {}) # pragma: no cover
IsAuthenticated = type('MockIsAuthenticated', (object,), {}) # pragma: no cover
ScopedRateThrottle = type('MockScopedRateThrottle', (object,), {}) # pragma: no cover
parsers = type('MockParsers', (object,), {'FormParser': object, 'JSONParser': object, 'MultiPartParser': object})() # pragma: no cover
renderers = type('MockRenderers', (object,), {'JSONRenderer': object})() # pragma: no cover

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
_l_(15052)

class FooView(APIView):
    _l_(15061)

    # The "injected" dependencies:
    permission_classes = (IsAuthenticated, )
    _l_(15053)
    throttle_classes = (ScopedRateThrottle, )
    _l_(15054)
    parser_classes = (parsers.FormParser, parsers.JSONParser, parsers.MultiPartParser)
    _l_(15055)
    renderer_classes = (renderers.JSONRenderer,)
    _l_(15056)

    def get(self, request, *args, **kwargs):
        _l_(15058)

        pass
        _l_(15057)

    def post(self, request, *args, **kwargs):
        _l_(15060)

        pass
        _l_(15059)

