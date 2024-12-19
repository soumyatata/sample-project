from flask import Flask,request,jsonify
from flask_cors import CORS 
import html


# Define CORS origins as a variable
CORS_ORIGINS = ["http://localhost:3000"]

app=Flask(__name__)
CORS(app, origins=CORS_ORIGINS)

def sanitize_html_input(input_string):
    return html.escape(input_string)

@app.route('/api/submit',methods=['POST'])

def submit_date():
    data=request.json
    if 'name' not in data or not data['name']:
        return jsonify({'error':'Name is required'}),400
    
    sanitized_name = sanitize_html_input(data['name'])
    return jsonify({'message':f"Hello {sanitized_name}!"}),200

if __name__=='__main__':
    app.run(debug=True)