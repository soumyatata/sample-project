from flask import Flask,request,jsonify
from flask_cors import CORS 
import html
import re
from database import insert_record,get_users,create_table


# Define CORS origins as a variable
CORS_ORIGINS = ["http://localhost:3000"]

app=Flask(__name__)
CORS(app, origins=CORS_ORIGINS)

def sanitize_html_input(input_string):
    return html.escape(input_string)

def is_validate_email(email):
    regex= r'^[a-zA-Z0-9]+([_.+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)$'
    return re.match(regex,email)

@app.route('/api/users',methods=['GET'])
def fetch_users():
    users=get_users()
    if not users:
        return jsonify({'error':'No users found'}),404
    return jsonify({'users':users}),200

@app.route('/api/submit',methods=['POST'])

def submit_date():
    data=request.json
   
    if 'name' not in data or not data['name']:
        return jsonify({'error':'Name is required'}),400
    if not isinstance(data['name'],str) :
        return jsonify({'error': 'Name must be a string'}),400
    if len(data['name']) < 5 or len(data['name']) > 30:
        return jsonify({'error':'Name length must be between 5 and 10 charcters'}),400
    
    if 'email' not in data or not data['email']:
        return jsonify({'error':'Email is required'}),400
    if not is_validate_email(data['email']):
        return jsonify({'error':'Invalid email format'}),400
    
    
    sanitized_name = sanitize_html_input(data['name'])
    success,error_message=insert_record(sanitized_name)

    if not success:
        return jsonify({'error': error_message}),400

    return jsonify({'message':f"Hello {sanitized_name}!"}),200

if __name__=='__main__':
    create_table()
    app.run(debug=True)