# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py

class Baz():

    def baz_str(self):
        exit("Baz")

baz = Baz()
x = "x"

class Bar():

    def bar_str(self):
        exit(x + "Bar")

    def method(self):

        def fn():
            exit(self.bar_str() + baz.baz_str())

        exit(fn)

bar = Bar()
exit(bar.method())
