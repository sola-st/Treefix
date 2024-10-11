import pytest # pragma: no cover
from lxml.etree import XSLTApplyError # pragma: no cover
import pandas as pd # pragma: no cover
import tempfile # pragma: no cover

geom_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}) # pragma: no cover
class TestManager: # pragma: no cover
    @staticmethod # pragma: no cover
    def ensure_clean(filename): # pragma: no cover
        class TempFileContextManager: # pragma: no cover
            def __init__(self, name): # pragma: no cover
                self.file = tempfile.NamedTemporaryFile(delete=False, suffix='.xml') # pragma: no cover
                self.name = self.file.name # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self.name # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                try: # pragma: no cover
                    self.file.close() # pragma: no cover
                finally: # pragma: no cover
                    try: # pragma: no cover
                        os.remove(self.name) # pragma: no cover
                    except OSError: # pragma: no cover
                        pass # pragma: no cover
        return TempFileContextManager(filename) # pragma: no cover
tm = TestManager() # pragma: no cover
def to_xml(df, path, stylesheet): # pragma: no cover
    # Simply creating an XML structure as a mock function # pragma: no cover
    with open(path, 'w') as f: # pragma: no cover
        f.write('<root></root>') # pragma: no cover
pd.DataFrame.to_xml = to_xml # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
try:
    from lxml.etree import XSLTApplyError
    _l_(21714)

except ImportError:
    pass

xsl = """\
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" encoding="utf-8" indent="yes" />
    <xsl:strip-space elements="*"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:copy-of select="document('non_existent.xml')/*"/>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>"""
_l_(21715)

with pytest.raises(XSLTApplyError, match=("Cannot resolve URI")):
    _l_(21718)

    with tm.ensure_clean("test.xml") as path:
        _l_(21717)

        geom_df.to_xml(path, stylesheet=xsl)
        _l_(21716)
