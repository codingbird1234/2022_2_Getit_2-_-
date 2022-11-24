import Input from "./pages/Input";
import Output from "./pages/Output";
import Login from "./pages/Login";
import {Routes,Route,Link} from "react-router-dom"

function App() {
  return (
    <div classname="App">
     <nav>
     <Link to="/login">로그인</Link> |
      <Link to="/input">입력</Link> |
      <Link to="/Output">조회</Link> 
     </nav>
   <Routes>
   <Route path="/login" element={<Login/>} />
    <Route path="/input" element={<Input/>} />
    <Route path="/Output" element={<Output/>} />
   </Routes>
   </div>
  );
}

export default App;
