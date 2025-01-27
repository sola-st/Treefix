# Extracted from ./data/repos/scrapy/scrapy/selector/unified.py
rt = XmlResponse if st == 'xml' else HtmlResponse
exit(rt(url='about:blank', encoding='utf-8',
          body=to_bytes(text, 'utf-8')))
