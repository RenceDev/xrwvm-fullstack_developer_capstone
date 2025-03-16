import { Routes, Route } from 'react-router-dom';
import Login from './components/Login/Login';
import Register from './components/Register/Register';  // Import Register component

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />  {/* Login route */}
      <Route path="/register" element={<Register />} />  {/* Register route */}
      {/* Other routes */}
    </Routes>
  );
}

export default App;
