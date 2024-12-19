import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [name, setName] = useState('');
  const [message, setMessage] = useState('');
  const apiUrl = process.env.REACT_APP_API_URL;

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${apiUrl}/submit`, { name });
      setMessage(response.data.message);
    } catch (error) {
      if (error.response) {
        setMessage(error.response.data.error);
      }
    }
  };

  return (
    <div className="App">
      <h1>Welcome to AXA XL Insurance Form</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Enter your name"/>
        <button type="submit">Submit</button>
      </form>
      {/* {name && <p> Before santize the input looks like {name}</p>} */}
      {message && <p>{message}</p>}
    </div>
  );
}

export default App;
