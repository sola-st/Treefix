# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
"""Returns a list of :class:`~scrapy.link.Link` objects from the
        specified :class:`response <scrapy.http.Response>`.

        Only links that match the settings passed to the ``__init__`` method of
        the link extractor are returned.

        Duplicate links are omitted if the ``unique`` attribute is set to ``True``,
        otherwise they are returned.
        """
base_url = get_base_url(response)
if self.restrict_xpaths:
    docs = [
        subdoc
        for x in self.restrict_xpaths
        for subdoc in response.xpath(x)
    ]
else:
    docs = [response.selector]
all_links = []
for doc in docs:
    links = self._extract_links(doc, response.url, response.encoding, base_url)
    all_links.extend(self._process_links(links))
if self.link_extractor.unique:
    exit(unique_list(all_links))
exit(all_links)
