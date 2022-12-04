
import sys
import argparse
from xml.etree import ElementTree

#defining the command line arguments
parser = argparse.ArgumentParser(description='Parses Nmap XML output into a modern HTML report.')
parser.add_argument('--xml', help='specifies the input XML file', required=True)
parser.add_argument('--html-output', help='specifies the output HTML file', required=True)
args = parser.parse_args()

#reading in the xml file
tree = ElementTree.parse(args.xml)
root = tree.getroot()

#creating the html file
html_file = open(args.html_output, "w")
html_file.write("<head>\n")
html_file.write("<title>Nmap Report</title>\n")
html_file.write("<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>\n")
html_file.write("<script>\n")
html_file.write("$(document).ready(function(){\n")
html_file.write("  $('#myTable').DataTable();\n")
html_file.write("});\n")
html_file.write("</script>\n")
html_file.write("<link rel='stylesheet' type='text/css' href='https://cdn.datatables.net/1.10.15/css/jquery.dataTables.min.css'>\n")
html_file.write("<script type='text/javascript' language='javascript' src='https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js'></script>\n")
html_file.write("<style>\n")
html_file.write("table {\n")
html_file.write("  font-family: arial, sans-serif;\n")
html_file.write("  border-collapse: collapse;\n")
html_file.write("  width: 100%;\n")
html_file.write("}\n")
html_file.write("\n")
html_file.write("td, th {\n")
html_file.write("  border: 1px solid #dddddd;\n")
html_file.write("  text-align: left;\n")
html_file.write("  padding: 8px;\n")
html_file.write("}\n")
html_file.write("\n")
html_file.write("tr:nth-child(even) {\n")
html_file.write("  background-color: #dddddd;\n")
html_file.write("}\n")
html_file.write("</style>\n")
html_file.write("</head>\n")
html_file.write("<body>\n")
html_file.write("<h2>Nmap Report</h2>\n")
html_file.write("<table id='myTable'>\n")
html_file.write("  <thead>\n")
html_file.write("  <tr>\n")
html_file.write("    <th>Host</th>\n")
html_file.write("    <th>Port</th>\n")
html_file.write("    <th>Service</th>\n")
html_file.write("    <th>Product</th>\n")
html_file.write("    <th>Version</th>\n")
html_file.write("    <th>Extrainfo</th>\n")
html_file.write("  </tr>\n")
html_file.write("  </thead>\n")

#parsing the xml file
for host in root.iter('host'):
  hostname = host.find('address').get('addr')
  for port in host.findall('ports/port'):
    port_number = port.get('portid')
    service = port.find('service').get('name')
    product = port.find('service').get('product')
    version = port.find('service').get('version')
    extrainfo = port.find('service').get('extrainfo')
    if product is None:
        product = ""
    if version is None:
        version = ""
    if extrainfo is None:
        extrainfo = ""
    html_file.write("  <tr>\n")
    html_file.write("    <td>" + hostname + "</td>\n")
    html_file.write("    <td>" + port_number + "</td>\n")
    html_file.write("    <td>" + service + "</td>\n")
    html_file.write("    <td>" + product + "</td>\n")
    html_file.write("    <td>" + version + "</td>\n")
    html_file.write("    <td>" + extrainfo + "</td>\n")
    html_file.write("  </tr>\n")

html_file.write("</table>\n")
html_file.write("</body>\n")
html_file.close()
