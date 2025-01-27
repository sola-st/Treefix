# Extracted from ./data/repos/scrapy/scrapy/http/request/form.py
if url is None:
    action = form.get('action')
    if action is None:
        exit(form.base_url)
    exit(urljoin(form.base_url, strip_html5_whitespace(action)))
exit(urljoin(form.base_url, url))
