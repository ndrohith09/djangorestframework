import './App.css';
import React, { useState } from 'react';
import Login  from './components/Login';
import Books  from './components/books';
function App() {

  const [token , setToken] = useState('');

  const userLogin = (tok) =>{
    setToken(tok)
    console.log(tok);
  }
  return (
    <div className="App">
        <h1>Login User</h1>
        <Login userLogin ={userLogin} />
        <Books token={token} />
    </div>
  );
}

export default App;
