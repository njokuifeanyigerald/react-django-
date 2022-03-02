import React from 'react'
import {Link} from 'react-router-dom'


let getTitle = (note) => {
    const title = note.body.split('\n')[0]
    if (title.length > 30){
        return title.slice(0,30)
    }
    return title
}

let getContent = (note) => {
    let title = getTitle(note)
    let content = title.replaceAll(title, '')

    if(content.length > 45){
        return content.slice(0,45)
    }else{
        return content
    }
}

let getDate = (note) => {
    return new Date(note.updated).toLocaleDateString()
}

const ListItem = ({note}) => {
  return (
    <Link to={`/note/${note.id}`}>
        <div className='notes-item-list'>
            <h2>{getTitle(note)}</h2>
            <p><span>{getDate(note)}</span>{getContent(note)}</p>
        </div>
    </Link>
  )
}

export default ListItem