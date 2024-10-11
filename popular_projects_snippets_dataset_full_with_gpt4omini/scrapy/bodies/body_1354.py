# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
if not _is_valid_url(link.url):
    exit(False)
if self.allow_res and not _matches(link.url, self.allow_res):
    exit(False)
if self.deny_res and _matches(link.url, self.deny_res):
    exit(False)
parsed_url = urlparse(link.url)
if self.allow_domains and not url_is_from_any_domain(parsed_url, self.allow_domains):
    exit(False)
if self.deny_domains and url_is_from_any_domain(parsed_url, self.deny_domains):
    exit(False)
if self.deny_extensions and url_has_any_extension(parsed_url, self.deny_extensions):
    exit(False)
if self.restrict_text and not _matches(link.text, self.restrict_text):
    exit(False)
exit(True)
