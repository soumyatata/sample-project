# AXA XL- Assessment

This project is a simple web application that demonstrates the use of a Python backend with Flask to handle a RESTful API endpoint, and a React frontend that interacts with the backend. The application sanitizes user input to prevent security vulnerabilities such as XSS attacks.

## Features

- Flask backend that accepts user input via a RESTful API
- Input sanitization to prevent XSS and other security risks
- React frontend with TypeScript to make POST requests to the backend
- Simple user interaction, displaying personalized messages

## Technologies Used

- **Frontend**:
  - React
  - Axios (for API requests)
  
- **Backend**:
  - Flask (Python)
  - Flask-CORS (to handle cross-origin requests)

## Setup Instructions

### Backend Setup (Flask)

1. Clone the repository:
  ```bash
   git clone https://github.com/soumyatata/axa-xl-insurance-assessment.git
   cd axa-xl-insurance-assessment/backend
  ```
2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Run the backend:
  ```bash
  python app.py
  ```
  The backend will be running at `http:127.0.0.1:5000`


### Frontend Setup (React)

1. Navigate to the frontend directory
  ```bash
    cd /frontend
  ```

2. Install dependecies:
  ```bash
    npm install
  ```

3. Start the React development server:

  ```bash
  npm start
  ```
The frontend will be available at `http://localhost:3000`.

### Key Points:
1. **Frontend `.env.development` file**: It’s essential to specify the `REACT_APP_API_URL` in the `.env.development` file for the React frontend to know where to make API calls.
2. **Backend API URL**: In this case, `REACT_APP_API_URL=http://127.0.0.1:5000/api` points to the backend API, ensuring React knows where to send the requests.

### Additional Note:
- Ensure that the **backend** is running before starting the **frontend**, as the frontend will try to connect to the backend.

**How to Use**
1. Open the frontend application in your browser.
2. Enter your name in the form and click the submit button
3. The backend will process the input, santize it, and return a personalized message.

**Input Santization**

-The backend uses HTML escaping to santize user input and prevent XSS attacks. The `sanitize_html_input` function ensures that potientially harmful HTML charcters are escaped.
