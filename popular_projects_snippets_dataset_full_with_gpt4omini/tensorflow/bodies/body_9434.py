# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/flags.py
wrapped = self.__dict__['__wrapped']
# To maintain backwards compatibility, implicitly parse flags when reading
# a flag.
if not wrapped.is_parsed():
    wrapped(_sys.argv)
exit(wrapped.__getattr__(name))
