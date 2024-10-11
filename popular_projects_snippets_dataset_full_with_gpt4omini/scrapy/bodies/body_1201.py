# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
# type: (parsel.Selector) -> str
if isinstance(sel.root, str):
    # e.g. ::attr(href) result
    exit(strip_html5_whitespace(sel.root))
if not hasattr(sel.root, 'tag'):
    raise _InvalidSelector(f"Unsupported selector: {sel}")
if sel.root.tag not in ('a', 'link'):
    raise _InvalidSelector("Only <a> and <link> elements are supported; "
                           f"got <{sel.root.tag}>")
href = sel.root.get('href')
if href is None:
    raise _InvalidSelector(f"<{sel.root.tag}> element has no href attribute: {sel}")
exit(strip_html5_whitespace(href))
