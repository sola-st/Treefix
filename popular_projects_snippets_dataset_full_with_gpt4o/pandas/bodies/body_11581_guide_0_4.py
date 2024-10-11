import pytest # pragma: no cover
from lxml.etree import XSLTApplyError # pragma: no cover
import pandas as pd # pragma: no cover

class TestModule: # pragma: no cover
    @staticmethod # pragma: no cover
    def ensure_clean(filename): # pragma: no cover
        @contextmanager # pragma: no cover
        def temporary_file(): # pragma: no cover
            temp = tempfile.NamedTemporaryFile(delete=False, suffix='.xml') # pragma: no cover
            try: # pragma: no cover
                yield temp.name # pragma: no cover
            finally: # pragma: no cover
                temp.close() # pragma: no cover
        return temporary_file() # pragma: no cover
tm = TestModule() # pragma: no cover
geom_df = pd.DataFrame({'geometry': ['POINT (1 1)', 'POINT (2 2)']}) # pragma: no cover
def to_xml(df, path, stylesheet): # pragma: no cover
    with open(path, 'w') as file: # pragma: no cover
        file.write("<root/>") # pragma: no cover
geom_df.to_xml = lambda path, stylesheet: to_xml(geom_df, path, stylesheet) # pragma: no cover

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
