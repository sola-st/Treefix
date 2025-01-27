# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
if self.unique:
    exit(unique_list(links, key=self.link_key))
exit(links)
