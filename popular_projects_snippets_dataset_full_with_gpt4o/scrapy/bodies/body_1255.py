# Extracted from ./data/repos/scrapy/scrapy/exporters.py
self.binary = options.pop('binary', True)
super()._configure(options, dont_fail)
if self.binary:
    warnings.warn(
        "PythonItemExporter will drop support for binary export in the future",
        ScrapyDeprecationWarning)
if not self.encoding:
    self.encoding = 'utf-8'
