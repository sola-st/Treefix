# Extracted from ./data/repos/scrapy/scrapy/http/request/form.py
"""Return a list of key-value pairs for the inputs found in the given form."""
try:
    formdata_keys = dict(formdata or ()).keys()
except (ValueError, TypeError):
    raise ValueError('formdata should be a dict or iterable of tuples')

if not formdata:
    formdata = []
inputs = form.xpath('descendant::textarea'
                    '|descendant::select'
                    '|descendant::input[not(@type) or @type['
                    ' not(re:test(., "^(?:submit|image|reset)$", "i"))'
                    ' and (../@checked or'
                    '  not(re:test(., "^(?:checkbox|radio)$", "i")))]]',
                    namespaces={"re": "http://exslt.org/regular-expressions"})
values = [
    (k, '' if v is None else v)
    for k, v in (_value(e) for e in inputs)
    if k and k not in formdata_keys
]

if not dont_click:
    clickable = _get_clickable(clickdata, form)
    if clickable and clickable[0] not in formdata and not clickable[0] is None:
        values.append(clickable)

if isinstance(formdata, dict):
    formdata = formdata.items()  # type: ignore[assignment]

values.extend((k, v) for k, v in formdata if v is not None)
exit(values)
