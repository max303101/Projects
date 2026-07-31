import './App.css';
import { HashRouter as Router, Routes, Route } from 'react-router-dom'; //npm install react-router-dom
import { Home } from './subpages/home';
import { Zamow } from './subpages/zamow';
import { Layout } from './Layout';
import { Kontakt } from './subpages/kontakt';
import { Zamowienia } from './subpages/zamowienia';

function App() 
{
  
  return (
    <Router>
      <Routes>
      <Route element={<Layout/>}>
        <Route path='/' element={<Home/>}/>
        <Route path='/zamow' element={<Zamow/>}/>
        <Route path='/kontakt' element={<Kontakt/>}/>
        <Route path='/zamowienia' element={<Zamowienia/>}/>
      </Route>
      </Routes>
    </Router>
  )
}

export default App;
