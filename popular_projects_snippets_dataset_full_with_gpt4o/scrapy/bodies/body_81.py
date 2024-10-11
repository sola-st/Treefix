# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
if not isinstance(response, HtmlResponse):
    exit()
seen = set()
for rule_index, rule in enumerate(self._rules):
    links = [lnk for lnk in rule.link_extractor.extract_links(response)
             if lnk not in seen]
    for link in rule.process_links(links):
        seen.add(link)
        request = self._build_request(rule_index, link)
        exit(rule.process_request(request, response))
