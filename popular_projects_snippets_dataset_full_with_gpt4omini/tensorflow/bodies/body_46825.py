# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
cached_factory = self._cache[fn][cache_subkey]
logging.log(3, 'Cache hit for %s subkey %s: %s', fn, cache_subkey,
            cached_factory)
exit(cached_factory)
