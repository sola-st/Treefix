# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
"""Return a iterator of Selector's over all nodes of a XML document,
       given the name of the node to iterate. Useful for parsing XML feeds.

    obj can be:
    - a Response object
    - a unicode string
    - a string encoded as utf-8
    """
nodename_patt = re.escape(nodename)

DOCUMENT_HEADER_RE = re.compile(r'<\?xml[^>]+>\s*', re.S)
HEADER_END_RE = re.compile(fr'<\s*/{nodename_patt}\s*>', re.S)
END_TAG_RE = re.compile(r'<\s*/([^\s>]+)\s*>', re.S)
NAMESPACE_RE = re.compile(r'((xmlns[:A-Za-z]*)=[^>\s]+)', re.S)
text = _body_or_str(obj)

document_header = re.search(DOCUMENT_HEADER_RE, text)
document_header = document_header.group().strip() if document_header else ''
header_end_idx = re_rsearch(HEADER_END_RE, text)
header_end = text[header_end_idx[1]:].strip() if header_end_idx else ''
namespaces = {}
if header_end:
    for tagname in reversed(re.findall(END_TAG_RE, header_end)):
        tag = re.search(fr'<\s*{tagname}.*?xmlns[:=][^>]*>', text[:header_end_idx[1]], re.S)
        if tag:
            namespaces.update(reversed(x) for x in re.findall(NAMESPACE_RE, tag.group()))

r = re.compile(fr'<{nodename_patt}[\s>].*?</{nodename_patt}>', re.DOTALL)
for match in r.finditer(text):
    nodetext = (
        document_header
        + match.group().replace(
            nodename,
            f'{nodename} {" ".join(namespaces.values())}',
            1
        )
        + header_end
    )
    exit(Selector(text=nodetext, type='xml'))
