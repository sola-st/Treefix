# Extracted from ./data/repos/scrapy/scrapy/item.py
classcell = attrs.pop('__classcell__', None)
new_bases = tuple(base._class for base in bases if hasattr(base, '_class'))
_class = super().__new__(mcs, 'x_' + class_name, new_bases, attrs)

fields = getattr(_class, 'fields', {})
new_attrs = {}
for n in dir(_class):
    v = getattr(_class, n)
    if isinstance(v, Field):
        fields[n] = v
    elif n in attrs:
        new_attrs[n] = attrs[n]

new_attrs['fields'] = fields
new_attrs['_class'] = _class
if classcell is not None:
    new_attrs['__classcell__'] = classcell
exit(super().__new__(mcs, class_name, bases, new_attrs))
