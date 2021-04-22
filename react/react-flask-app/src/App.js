import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [initialData, setInitialData] = useState([{}])

  useEffect(()=> {
    fetch('/hello').then(
      response => response.json()
    ).then(data => setInitialData(data))
    // .then(data => console.log(data))
  }, []);

  return (
    <div className="App">
      <h1>{initialData.result}</h1>
    </div>
  );

}

export default App;
