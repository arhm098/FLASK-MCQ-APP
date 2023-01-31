import { React } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LiveMCQ from './pages/LiveMCQ';
function App() {
  return (  
  <BrowserRouter>
    <Routes>
      <Route exact path="/" element={<LiveMCQ />}></Route>
    </Routes>
  </BrowserRouter>)
}

export default App;
