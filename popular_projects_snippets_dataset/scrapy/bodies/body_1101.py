# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
case = _create_testcase(method, 'errback')
exc_info = failure.type, failure.value, failure.getTracebackObject()
results.addError(case, exc_info)
