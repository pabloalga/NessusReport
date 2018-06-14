# https://static.tenable.com/documentation/nessus_v2_file_format.pdf
# https://docs.python.org/2/library/xml.dom.html
# https://docs.python.org/2/library/xml.dom.minidom.html
#

from xml.dom.minidom import parse
import xml.dom.minidom
import sys

DOM_nessus = xml.dom.minidom.parse(sys.argv[1])

def nessus_xml(doc):
    for structure in doc.childNodes:
        if structure.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
            print "%s: " % structure.tagName,
            if structure.hasChildNodes() and structure.firstChild.nodeType == xml.dom.minidom.Node.TEXT_NODE:
                print "%s" % structure.firstChild.data
            nessus_xml(structure)

nessus_xml(DOM_nessus)
