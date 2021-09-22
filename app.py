from flask import Flask;
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")+' Hello there!!!!'

#
app.run(debug=True,host='0.0.0.0', port=8085)