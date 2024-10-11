# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
self.testcase_pre = _create_testcase(method, f'@{self.name} pre-hook')
self.testcase_post = _create_testcase(method, f'@{self.name} post-hook')
self.args = args
