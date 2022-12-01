from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    
    def do_GET(self):
        print("Hola desde el get")
        if "/sensor1_temp" in self.path:
            sensor1_temp = slef.path.split("=")[1]
            print("La temperatura es {}".format(sensor1_temp))
            self._set_response()
            self.wfile.write("Hola este es mi super server. GET request for {}".format(self.path).encode('utf-8'))
            #........................................
           
            collectionName = u'sensor_Samuel_${0}'
            
            temperatura_ref = db.collection(collectionName).document('temperatura')
            temperatura_doc = temperatura_ref.get()
            temperatura_data = temperatura_doc.to_dict()
    
            if temperatura_data == None:
                temperatura_ref.set({
                    u'temperatura.2': sensor1_temp,
                })
            else:
                temperatura_ref.update({
                    u'temperatura_medida': temperatura_data[u'temperatura_medida'],
                    })  
            #........................................
port = 8080
server_address = ('', port)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()