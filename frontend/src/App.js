import NoteListPage from './pages/NoteListPage';
import { Route, BrowserRouter as Router, Routes} from 'react-router-dom';
import React from 'react';
import Header from './components/Header';
// css
import './App.css'
import NotePage from './pages/NotePage';


function App() {
  return (
    <div className="container dark">
      <div className='app'>
        <Router>          
          <Header />
          <Routes>
            <Route path="/" exact element={<NoteListPage/>} />
            <Route path="/note/:id" element={<NotePage/>} />
          </Routes>
        </Router>
      </div>
      
    </div>
  );
}

export default App;
