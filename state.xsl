<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text" />

    <!-- Define a template to match the root element -->
    <xsl:template match="/">
        <!-- Call the template to concatenate event attributes -->
        <xsl:call-template name="events"/>
    </xsl:template>

    <!-- Define a template to concatenate event attributes -->
    <xsl:template name="events">
        <!-- Define a variable to store concatenated event values -->
        <xsl:variable name="events">
            <!-- Select all elements with an attribute named "event" -->
            <xsl:text>event = [</xsl:text>
            <xsl:for-each select="//@event">
                <!-- Append the value of the "event" attribute to the variable -->
                <xsl:text>"</xsl:text><xsl:value-of select="."/><xsl:text>"</xsl:text>
                <!-- Add a comma if this is not the last attribute -->
                <xsl:if test="position() &lt; last()">, </xsl:if>
            </xsl:for-each>
            <xsl:text>]</xsl:text>
        </xsl:variable>

        <!-- Output the concatenated values -->
        <xsl:value-of select="$events"/>
    </xsl:template>

</xsl:stylesheet>
