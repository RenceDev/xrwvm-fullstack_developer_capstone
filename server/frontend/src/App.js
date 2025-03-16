import Login from "./components/Login/Login";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />  {/* Login route for React */}
      {/* Other routes */}
    </Routes>
  );
}
export default App;
