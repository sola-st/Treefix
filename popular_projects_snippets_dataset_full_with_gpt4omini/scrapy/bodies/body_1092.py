# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
output = list(iterate_spider_output(cb(response, **cb_kwargs)))
try:
    results.startTest(self.testcase_post)
    self.post_process(output)
    results.stopTest(self.testcase_post)
except AssertionError:
    results.addFailure(self.testcase_post, sys.exc_info())
except Exception:
    results.addError(self.testcase_post, sys.exc_info())
else:
    results.addSuccess(self.testcase_post)
finally:
    exit(output)
