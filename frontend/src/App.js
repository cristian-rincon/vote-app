import './App.css';
import React, { Component } from 'react';
import axios from 'axios';
import questions from './mocks/questions';

const headers = {"Access-Control-Allow-Origin": "*"}


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      questions: questions
    };
  }

  componentDidMount() {
    this.refreshData();
  }

  refreshData() {
    axios
      .get('http://localhost:8000/', { headers: headers })
      .then(response => {
        this.setState({
          questions: response.data
        });
      })
      .catch(error => {
        console.log(`Error: ${error}`);
      });
  }


  // renderQuestions() {
  //   return this.state.questions.results.map(question => {
  //     return (
  //       <div key={question.id}>
  //         <h3>{question.question_text}</h3>
  //         <ul>
  //           {question.choices.map(choice => {
  //             return (
  //               <li key={choice.id}>
  //                 {choice.choice_text}
  //               </li>
  //             );
  //           })}
  //         </ul>
  //       </div>
  //     );
  //   }
  //   );
  // }

  renderHome() {
    return (
      <div className="">
        <h1>Welcome to the Poll App!</h1>
        <p>
          This is a simple poll app that allows you to create polls and vote on them.
        </p>
        <p>
          You can create a poll by clicking the "Create Poll" button on the top right.
        </p>
        <p>
          You can view all of your polls by clicking the "View Polls" button on the top right.
        </p>
        <p>
          You can view all of your votes by clicking the "View Votes" button on the top right.
        </p>
      </div>
    );
  }

  render() {
    return (
      <main className='content'>
        {/* <h1>Preguntas</h1> */}
        {/* {this.renderQuestions()} */}
        {this.renderHome()}
      </main>
    )
  }
}

export default App;
