import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import TextRandom from './components/TextRandom';
import PeselValidator from './components/PeselCheck';
import { Home } from './components/Home';
function App() {
  return (
    <div className="App">
      <Router>
          <Routes>
              <Route element={<Home />} path="/" />
              <Route element={<TextRandom />} path="/text-random" exact/>
              <Route element={<PeselValidator/>} path="/pesel-validator"/>
              </Routes>
      </Router>
    </div>
  );
}

export default App;
