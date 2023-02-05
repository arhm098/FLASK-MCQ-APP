import { React } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LiveMCQ from './pages/LiveMCQ';
import Login from "./pages/Login";
function App() {
  return (  
  <BrowserRouter>
    <Routes>
      <Route exact path="/" element={<Login />}></Route>
    </Routes>
  </BrowserRouter>)
}

export default App;
