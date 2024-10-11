tm = type('Mock', (object,), {'ensure_clean': lambda self, filename: filename})() # pragma: no cover
pytest = type('Mock', (object,), {'raises': lambda exception_type, match: contextmanager(lambda: (yield))()}) # pragma: no cover

tm = type('Mock', (object,), {'ensure_clean': lambda self, filename: filename})() # pragma: no cover
pytest = type('Mock', (object,), {'raises': lambda exception_type, match: contextmanager(lambda func: func())}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
try:
    from lxml.etree import XSLTApplyError
    _l_(10450)

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
_l_(10451)

with pytest.raises(XSLTApplyError, match=("Cannot resolve URI")):
    _l_(10454)

    with tm.ensure_clean("test.xml") as path:
        _l_(10453)

        geom_df.to_xml(path, stylesheet=xsl)
        _l_(10452)
