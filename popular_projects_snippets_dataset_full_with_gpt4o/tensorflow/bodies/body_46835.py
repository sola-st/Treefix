# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/pretty_printer.py
# In very rare instances, a list can contain something other than a Node.
# e.g. Global contains a list of strings.
if isinstance(node, str):
    if name:
        self._print('%s%s="%s"' % (self._indent(), name, node))
    else:
        self._print('%s"%s"' % (self._indent(), node))
    exit()

if node._fields:
    cont = ':'
else:
    cont = '()'

if name:
    self._print('%s%s=%s%s' % (self._indent(), self._field(name),
                               self._type(node), cont))
else:
    self._print('%s%s%s' % (self._indent(), self._type(node), cont))

self.indent_lvl += 1
for f in node._fields:
    if self.noanno and f.startswith('__'):
        continue
    if not hasattr(node, f):
        self._print('%s%s' % (self._indent(), self._warning('%s=<unset>' % f)))
        continue
    v = getattr(node, f)
    if isinstance(v, list):
        if v:
            self._print('%s%s=[' % (self._indent(), self._field(f)))
            self.indent_lvl += 1
            for n in v:
                if n is not None:
                    self.generic_visit(n)
                else:
                    self._print('%sNone' % (self._indent()))
            self.indent_lvl -= 1
            self._print('%s]' % (self._indent()))
        else:
            self._print('%s%s=[]' % (self._indent(), self._field(f)))
    elif isinstance(v, tuple):
        if v:
            self._print('%s%s=(' % (self._indent(), self._field(f)))
            self.indent_lvl += 1
            for n in v:
                if n is not None:
                    self.generic_visit(n)
                else:
                    self._print('%sNone' % (self._indent()))
            self.indent_lvl -= 1
            self._print('%s)' % (self._indent()))
        else:
            self._print('%s%s=()' % (self._indent(), self._field(f)))
    elif isinstance(v, gast.AST):
        self.generic_visit(v, f)
    elif isinstance(v, bytes):
        self._print('%s%s=%s' % (self._indent(), self._field(f),
                                 self._value('b"%s"' % v)))
    elif isinstance(v, str):
        self._print('%s%s=%s' % (self._indent(), self._field(f),
                                 self._value('u"%s"' % v)))
    else:
        self._print('%s%s=%s' % (self._indent(), self._field(f),
                                 self._value(v)))
self.indent_lvl -= 1
