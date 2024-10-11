# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# see gh-16928

class ErrorThread(threading.Thread):
    def run(self):
        try:
            super().run()
        except Exception as err:
            self.err = err
        else:
            self.err = None

        # force import check by reinitalising global vars in html.py
reload(pandas.io.html)

filename = datapath("io", "data", "html", "valid_markup.html")
helper_thread1 = ErrorThread(target=self.read_html, args=(filename,))
helper_thread2 = ErrorThread(target=self.read_html, args=(filename,))

helper_thread1.start()
helper_thread2.start()

while helper_thread1.is_alive() or helper_thread2.is_alive():
    pass
assert None is helper_thread1.err is helper_thread2.err
