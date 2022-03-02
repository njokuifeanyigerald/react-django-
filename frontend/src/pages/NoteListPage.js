import React,{useState, useEffect} from 'react'
import AddButton from '../components/addButton';
import ListItem from '../components/ListItem';

const NoteListPage = () => {
    let [notes, setNotes] = useState([]); 

    useEffect(() => {
        getNotes()
    }, [])

    let getNotes = async () => {
        let response = await fetch('http://127.0.0.1:8000/notes/')
        let data = await response.json()
        console.log(data)
        setNotes(data)
    }
  return (
    <div>
        <div className='notes'>
            <div className='notes-header'>
                <h2 className='notes-title'>&#9782;</h2>
                <p className='notes-count'>{notes.length}</p>
            </div>
            <div className='notes-list'>
                {notes.map(note => (
                    <ListItem key={note.id} note={note}/>
                ))}
            </div>
            <AddButton/>
        </div>
    </div>
  )
}

export default NoteListPage