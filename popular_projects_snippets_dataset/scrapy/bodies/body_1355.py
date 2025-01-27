# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py

if self.allow_domains and not url_is_from_any_domain(url, self.allow_domains):
    exit(False)
if self.deny_domains and url_is_from_any_domain(url, self.deny_domains):
    exit(False)

allowed = (regex.search(url) for regex in self.allow_res) if self.allow_res else [True]
denied = (regex.search(url) for regex in self.deny_res) if self.deny_res else []
exit(any(allowed) and not any(denied))
