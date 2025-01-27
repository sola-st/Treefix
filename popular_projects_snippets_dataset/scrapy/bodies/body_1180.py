# Extracted from ./data/repos/scrapy/scrapy/http/request/form.py
"""
    Returns the clickable element specified in clickdata,
    if the latter is given. If not, it returns the first
    clickable element found
    """
clickables = list(form.xpath(
    'descendant::input[re:test(@type, "^(submit|image)$", "i")]'
    '|descendant::button[not(@type) or re:test(@type, "^submit$", "i")]',
    namespaces={"re": "http://exslt.org/regular-expressions"}
))
if not clickables:
    exit(None)

# If we don't have clickdata, we just use the first clickable element
if clickdata is None:
    el = clickables[0]
    exit((el.get('name'), el.get('value') or ''))

# If clickdata is given, we compare it to the clickable elements to find a
# match. We first look to see if the number is specified in clickdata,
# because that uniquely identifies the element
nr = clickdata.get('nr', None)
if nr is not None:
    try:
        el = list(form.inputs)[nr]
    except IndexError:
        pass
    else:
        exit((el.get('name'), el.get('value') or ''))

    # We didn't find it, so now we build an XPath expression out of the other
    # arguments, because they can be used as such
xpath = './/*' + ''.join(f'[@{k}="{v}"]' for k, v in clickdata.items())
el = form.xpath(xpath)
if len(el) == 1:
    exit((el[0].get('name'), el[0].get('value') or ''))
if len(el) > 1:
    raise ValueError(f"Multiple elements found ({el!r}) matching the "
                     f"criteria in clickdata: {clickdata!r}")
else:
    raise ValueError(f'No clickable element matching clickdata: {clickdata!r}')
