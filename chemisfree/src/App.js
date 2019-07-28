import React, { Component } from 'react'
import './App.css';
import axios from 'axios'

class App extends Component {

  constructor () {
	
    super()  
this.state = {
		formula: '',
	}	
	this.handleClick = this.handleClick.bind(this)
	this.handleClick2 = this.handleClick2.bind(this)
	this.handleChange = this.handleChange.bind(this);
	
	
  } 
  
  handleChange(event) {
  this.setState({value: event.target.value});
  event.preventDefault()

}
handleClick () {
	
	
    axios.get('http://localhost:5000/molarmass/'.concat(this.state.value)).then(response => this.setState({value: JSON.stringify(response.data).replace(/[`~!@#$%^&*()_|+\-=?;'",<>\{\}\[\]\\\/]/gi, '')}))
  }  
handleClick2 () {
    axios.get('http://localhost:5000/combust/'.concat(this.state.value)).then(response => this.setState({value: JSON.stringify(response.data).replace(/[`~!@#$%^&*()_|=?;'",<\{\}\[\]\\\/]/gi, '')}))
  } 
  render () {
    return (
<div>
	<div className='App-header'>
	<p>
		Welcome to Chemisfree- a chemistry tool for students
	</p>
	
	</div>
	<form className ='form'>
  <label>
    Enter Formula:
    <input type="text" name="formula" value={this.state.value} onChange={event => this.handleChange(event)}/>
  </label>
  <button className='button' type="button" onClick={this.handleClick}>
          Calculate Molar Mass
        </button>
  
		
		<button className = 'button2' type="button" onClick={this.handleClick2}>
          Calculate Combustion reaction
        </button>
</form>
	<h1>
	{this.state.value}
	</h1>
</div>
	  
	  
    )
  }
}export default App