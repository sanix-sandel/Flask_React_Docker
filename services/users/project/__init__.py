from flask import Flask, jsonify

app=Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/greet', methods=['GET'])
def home():
    return jsonify({
        'status':'success',
        'message':'Hello !'
    })