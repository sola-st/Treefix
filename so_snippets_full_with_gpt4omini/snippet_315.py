# Extracted from https://stackoverflow.com/questions/70528/why-are-pythons-private-methods-not-actually-private
class Foo(object):
class Bar(Foo):
x = Bar()
x.foo()
42
x.bar()
21
print x.__dict__
{'_Bar__baz': 21, '_Foo__baz': 42}

