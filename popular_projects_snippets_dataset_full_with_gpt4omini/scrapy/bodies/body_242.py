# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
if not _stdout:
    _stdout = sys.stdout.buffer
self._stdout = _stdout
if feed_options and feed_options.get('overwrite', False) is True:
    logger.warning('Standard output (stdout) storage does not support '
                   'overwriting. To suppress this warning, remove the '
                   'overwrite option from your FEEDS setting, or set '
                   'it to False.')
