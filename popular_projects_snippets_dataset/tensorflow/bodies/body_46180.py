# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info.py
if self.loc.filename:
    exit('{}:{}:{}'.format(
        os.path.split(self.loc.filename)[1], self.loc.lineno,
        self.loc.col_offset))
exit('<no file>:{}:{}'.format(self.loc.lineno, self.loc.col_offset))
