# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
requests = []
for method in self.tested_methods_from_spidercls(type(spider)):
    bound_method = spider.__getattribute__(method)
    try:
        requests.append(self.from_method(bound_method, results))
    except Exception:
        case = _create_testcase(bound_method, 'contract')
        results.addError(case, sys.exc_info())

exit(requests)
