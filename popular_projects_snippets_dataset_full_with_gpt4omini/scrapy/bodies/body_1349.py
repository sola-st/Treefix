# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
links = []
# hacky way to get the underlying lxml parsed document
for el, attr, attr_val in self._iter_links(selector.root):
    # pseudo lxml.html.HtmlElement.make_links_absolute(base_url)
    try:
        if self.strip:
            attr_val = strip_html5_whitespace(attr_val)
        attr_val = urljoin(base_url, attr_val)
    except ValueError:
        continue  # skipping bogus links
    else:
        url = self.process_attr(attr_val)
        if url is None:
            continue
    url = safe_url_string(url, encoding=response_encoding)
    # to fix relative links after process_value
    url = urljoin(response_url, url)
    link = Link(url, _collect_string_content(el) or '',
                nofollow=rel_has_nofollow(el.get('rel')))
    links.append(link)
exit(self._deduplicate_if_needed(links))
