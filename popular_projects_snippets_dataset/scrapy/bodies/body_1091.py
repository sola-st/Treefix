# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
if hasattr(self, 'pre_process'):
    cb = request.callback

    @wraps(cb)
    def wrapper(response, **cb_kwargs):
        try:
            results.startTest(self.testcase_pre)
            self.pre_process(response)
            results.stopTest(self.testcase_pre)
        except AssertionError:
            results.addFailure(self.testcase_pre, sys.exc_info())
        except Exception:
            results.addError(self.testcase_pre, sys.exc_info())
        else:
            results.addSuccess(self.testcase_pre)
        finally:
            exit(list(iterate_spider_output(cb(response, **cb_kwargs))))

    request.callback = wrapper

exit(request)
