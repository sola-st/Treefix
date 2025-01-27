# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
tags, attrs = set(arg_to_iter(tags)), set(arg_to_iter(attrs))
self.link_extractor = LxmlParserLinkExtractor(
    tag=partial(operator.contains, tags),
    attr=partial(operator.contains, attrs),
    unique=unique,
    process=process_value,
    strip=strip,
    canonicalized=canonicalize
)
self.allow_res = [x if isinstance(x, _re_type) else re.compile(x)
                  for x in arg_to_iter(allow)]
self.deny_res = [x if isinstance(x, _re_type) else re.compile(x)
                 for x in arg_to_iter(deny)]

self.allow_domains = set(arg_to_iter(allow_domains))
self.deny_domains = set(arg_to_iter(deny_domains))

self.restrict_xpaths = tuple(arg_to_iter(restrict_xpaths))
self.restrict_xpaths += tuple(map(self._csstranslator.css_to_xpath,
                                  arg_to_iter(restrict_css)))

if deny_extensions is None:
    deny_extensions = IGNORED_EXTENSIONS
self.canonicalize = canonicalize
self.deny_extensions = {'.' + e for e in arg_to_iter(deny_extensions)}
self.restrict_text = [x if isinstance(x, _re_type) else re.compile(x)
                      for x in arg_to_iter(restrict_text)]
