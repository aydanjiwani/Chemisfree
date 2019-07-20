import React, { Component } from 'react'
import './App.css';
import axios from 'axios'

class App extends Component {

  constructor () {
    super()    
	this.handleClick = this.handleClick.bind(this)
	
  } 
handleClick () {
    axios.get('http://localhost:5000/combust/C6H12O6').then(response => console.log(response))
  }  
  render () {
    return (
<div>
	<div className='App-header'>
	<p>
		Welcome to Chemisfree- a chemistry tool for students
	</p>
	</div>
      <div className='button__container'>
        <button className='button' onClick={this.handleClick}>
          Calculate Molar Mass
        </button>
  
		
		<button className = 'button' onClick={this.handleClick}>
          Calculate Combustion reaction
        </button>
		
		
	  </div>
	
</div>
	  
	  
    )
  }
}export default App