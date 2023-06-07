import qrcode
import base64
from flask import Flask
from flask import request
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def root():
   return '''<form action="/qr" method="GET">
      <input type="text" name="msgs" placeholder="Enter text"/>
      <input type="submit" value="QR-code"/>
   </form>'''


@app.route("/qr")
def qr():
   msg = request.args.get('msgs')
   img = qrcode.make(msg)
   
   buffer = BytesIO()
   img.save(buffer, format="png")
 
   img64 = base64.b64encode(buffer.getvalue())
   return f'<img src="data:image/png;base64, {img64.decode()}" alt="qrcode" />'


if __name__ == "__main__":
   app.run(host='0.0.0.0')
