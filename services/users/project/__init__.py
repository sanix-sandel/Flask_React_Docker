import os
from flask import Flask, jsonify

app=Flask(__name__)

app_settings=os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

@app.route('/users/greet', methods=['GET'])
def home():
    
    return jsonify({
        'status':'success',
        'message':'Hello !'
    })