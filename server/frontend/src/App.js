import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Register from './Register';
import Home from './Home'; // Assuming you have a Home component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        {/* Add other routes here */}
      </Routes>
    </Router>
  );
}

export default App;
