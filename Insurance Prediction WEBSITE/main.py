from flask import Flask
from public import public
from api import api
from admin import admin

app=Flask(__name__)
app.secret_key="key"
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(api,url_prefix="/api")
app.register_blueprint(public)




app.run(debug=True,port=5073,host="0.0.0.0")