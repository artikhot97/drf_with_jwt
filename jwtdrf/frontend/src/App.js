import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import { useSelector } from "react-redux";
import selectUser from "./features/userSlice";
import Login from "./Components/Login";
import Logout from "./Components/Logout";
import NavComponent from "./Components/NavComponent";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Home from "./Components/Home";
import Register from "./Components/Register";
import "./index.css";
import axios from "axios";
class App extends Component {
  // const user = useSelector(sesslectUser);
  // return <div className="App">{user ? <Logout /> : <Login />}</div>;
  state = {};
  componentDidMount = () => {
    axios.get("user").then(
      (res) => {
        this.setUser(res.data);
      },
      (err) => {
        console.log(err);
      }
    );
  };
  setUser = (user) => {
    this.setState({
      user: user,
    });
  };
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <NavComponent user={this.state.user} setUser={this.setUser} />
          <div className="auth-wrapper">
            <div className="auth-inner">
              <Switch>
                <Route
                  exact
                  path="/"
                  component={() => <Home user={this.state.user} />}
                />
                <Route
                  exact
                  path="/login"
                  component={() => <Login setUser={this.setUser} />}
                />
                <Route exact path="/register" component={Register} />
              </Switch>
            </div>
          </div>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
