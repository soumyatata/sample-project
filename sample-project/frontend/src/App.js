import React, { useState,useEffect } from 'react';
import axios from 'axios';

function App() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [users, setUsers]=useState('');
  const [message, setMessage] = useState('');
  const apiUrl = process.env.REACT_APP_API_URL;

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${apiUrl}/submit`, { name,email });
      setMessage(response.data.message);
    } catch (error) {
      if (error.response) {
        setMessage(error.response.data.error);
      }
    }
  };

  const fetchUsers= async()=>{
    try {
      const response =await axios.get(`${apiUrl}/users`);
      setUsers(response.data.users);
    }catch (error) {
      if (error.response) {
        setMessage(error.response.data.error);
      }
    }
  };

  useEffect(()=>{
    fetchUsers();
  },[]);

  return (
    <div className="App">
      <h1>Welcome to AXA XL Insurance Form</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Enter your name"/>
        <br/>
        <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Enter your email"/>
        <br/>
        <button type="submit">Submit</button>
      </form>
      {/* {name && <p> Before santize the input looks like {name}</p>} */}
      {message && <p>{message}</p>}

      <h3> View existing User</h3>
      <ul>
        {users.length > 0 ? (
          users.map((user,index)=>(
            <li key={index}>
              {user.name}
            </li>
          ))
        ) : (<p>No users available</p>)}
      </ul>
      

    </div>
  );
}

export default App;
