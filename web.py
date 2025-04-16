from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
    <head>
        <title>TCP/IP Layers and Protocols</title>
    </head>
    <body>
        <h1 align="center">TCP/IP LAYER and Protocols</h1> 
        <table border="1px" align="center">
            <tr>
                <th>S.No</th>
                <th>LAYERS</th>
                <th>PROTOCOLS</th>
            </tr>
            <tr>
                <td align="center">01.</td>
                <td align="center">Application Layer</td>
                <td align="center">HTTP, RDP, DNS, SMTP, Telnet, SNMP</td>
            </tr>
            <tr>
                <td align="center">02.</td>
                <td align="center">Transport Layer</td>
                <td align="center">TCP, UDP</td>
            </tr>
            <tr>
                <td align="center">03.</td>
                <td align="center">Internet Layer</td>
                <td align="center">ICMP, IGMP, ARP, IPSec</td>
            </tr>
            <tr>
                <td align="center">04.</td>
                <td align="center">Network Access Layer</td>
                <td align="center">Ethernet, Token Ring</td>
            </tr>
        </table>
    </body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
