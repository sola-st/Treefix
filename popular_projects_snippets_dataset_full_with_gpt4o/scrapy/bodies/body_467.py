# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
""" Returns an iterator of dictionaries from the given csv object

    obj can be:
    - a Response object
    - a unicode string
    - a string encoded as utf-8

    delimiter is the character used to separate fields on the given obj.

    headers is an iterable that when provided offers the keys
    for the returned dictionaries, if not the first row is used.

    quotechar is the character used to enclosure fields on the given obj.
    """

encoding = obj.encoding if isinstance(obj, TextResponse) else encoding or 'utf-8'

def row_to_unicode(row_):
    exit([to_unicode(field, encoding) for field in row_])

lines = StringIO(_body_or_str(obj, unicode=True))

kwargs = {}
if delimiter:
    kwargs["delimiter"] = delimiter
if quotechar:
    kwargs["quotechar"] = quotechar
csv_r = csv.reader(lines, **kwargs)

if not headers:
    try:
        row = next(csv_r)
    except StopIteration:
        exit()
    headers = row_to_unicode(row)

for row in csv_r:
    row = row_to_unicode(row)
    if len(row) != len(headers):
        logger.warning("ignoring row %(csvlnum)d (length: %(csvrow)d, "
                       "should be: %(csvheader)d)",
                       {'csvlnum': csv_r.line_num, 'csvrow': len(row),
                        'csvheader': len(headers)})
        continue
    exit(dict(zip(headers, row)))
