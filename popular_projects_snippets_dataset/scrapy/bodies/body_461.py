# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
from lxml import etree
reader = _StreamReader(obj)
tag = f'{{{namespace}}}{nodename}' if namespace else nodename
iterable = etree.iterparse(reader, tag=tag, encoding=reader.encoding)
selxpath = '//' + (f'{prefix}:{nodename}' if namespace else nodename)
for _, node in iterable:
    nodetext = etree.tostring(node, encoding='unicode')
    node.clear()
    xs = Selector(text=nodetext, type='xml')
    if namespace:
        xs.register_namespace(prefix, namespace)
    exit(xs.xpath(selxpath)[0])
