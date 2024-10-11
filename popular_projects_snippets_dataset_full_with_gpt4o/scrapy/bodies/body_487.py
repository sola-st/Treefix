# Extracted from ./data/repos/scrapy/scrapy/utils/log.py
"""
    Initialize logging defaults for Scrapy.

    :param settings: settings used to create and configure a handler for the
        root logger (default: None).
    :type settings: dict, :class:`~scrapy.settings.Settings` object or ``None``

    :param install_root_handler: whether to install root logging handler
        (default: True)
    :type install_root_handler: bool

    This function does:

    - Route warnings and twisted logging through Python standard logging
    - Assign DEBUG and ERROR level to Scrapy and Twisted loggers respectively
    - Route stdout to log if LOG_STDOUT setting is True

    When ``install_root_handler`` is True (default), this function also
    creates a handler for the root logger according to given settings
    (see :ref:`topics-logging-settings`). You can override default options
    using ``settings`` argument. When ``settings`` is empty or None, defaults
    are used.
    """
if not sys.warnoptions:
    # Route warnings through python logging
    logging.captureWarnings(True)

observer = twisted_log.PythonLoggingObserver('twisted')
observer.start()

dictConfig(DEFAULT_LOGGING)

if isinstance(settings, dict) or settings is None:
    settings = Settings(settings)

if settings.getbool('LOG_STDOUT'):
    sys.stdout = StreamLogger(logging.getLogger('stdout'))

if install_root_handler:
    install_scrapy_root_handler(settings)
