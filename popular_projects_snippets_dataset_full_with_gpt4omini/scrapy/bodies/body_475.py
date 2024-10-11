# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
"""Construct a class instance using its ``from_crawler`` or
    ``from_settings`` constructors, if available.

    At least one of ``settings`` and ``crawler`` needs to be different from
    ``None``. If ``settings `` is ``None``, ``crawler.settings`` will be used.
    If ``crawler`` is ``None``, only the ``from_settings`` constructor will be
    tried.

    ``*args`` and ``**kwargs`` are forwarded to the constructors.

    Raises ``ValueError`` if both ``settings`` and ``crawler`` are ``None``.

    .. versionchanged:: 2.2
       Raises ``TypeError`` if the resulting instance is ``None`` (e.g. if an
       extension has not been implemented correctly).
    """
if settings is None:
    if crawler is None:
        raise ValueError("Specify at least one of settings and crawler.")
    settings = crawler.settings
if crawler and hasattr(objcls, 'from_crawler'):
    instance = objcls.from_crawler(crawler, *args, **kwargs)
    method_name = 'from_crawler'
elif hasattr(objcls, 'from_settings'):
    instance = objcls.from_settings(settings, *args, **kwargs)
    method_name = 'from_settings'
else:
    instance = objcls(*args, **kwargs)
    method_name = '__new__'
if instance is None:
    raise TypeError(f"{objcls.__qualname__}.{method_name} returned None")
exit(instance)
