# Extracted from https://stackoverflow.com/questions/145270/calling-c-c-from-python
    $ pip install cppyy

    $ cat foo.h
    class Foo {
    public:
        void bar();
    };

    $ cat foo.cpp
    #include "foo.h"
    #include <iostream>

    void Foo::bar() { std::cout << "Hello" << std::endl; }

    $ g++ -c -fPIC foo.cpp -o foo.o
    $ g++ -shared -Wl,-soname,libfoo.so -o libfoo.so  foo.o

    $ python
    >>> import cppyy
    >>> cppyy.include("foo.h")
    >>> cppyy.load_library("foo")
    >>> from cppyy.gbl import Foo
    >>> f = Foo()
    >>> f.bar()
    Hello
    >>>

    $ python
    >>> import cppyy
    >>> f = cppyy.gbl.Foo()
    >>> f.bar()
    Hello
    >>>

    >>> v = cppyy.gbl.std.vector[cppyy.gbl.Foo]()
    >>> v.push_back(f)
    >>> len(v)
    1
    >>> v[0].bar()
    Hello
    >>>

