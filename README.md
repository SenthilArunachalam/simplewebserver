# EX01 Developing a Simple Webserver
## Date:16.04.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
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

~~~

## OUTPUT:
![image](https://github.com/user-attachments/assets/c613a16f-e789-464c-9918-73ada3e6f76f)


![alt text](<Screenshot 2025-04-16 111838.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
