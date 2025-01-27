# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from lxml.etree import XSLTApplyError

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

kml = datapath("io", "data", "xml", "cta_rail_lines.kml")

with pytest.raises(XSLTApplyError, match=("Cannot resolve URI")):
    read_xml(kml, stylesheet=xsl)
