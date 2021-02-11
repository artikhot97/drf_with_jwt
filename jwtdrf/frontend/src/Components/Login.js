import { Component } from "react";
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import login from "../features/userSlice";
import "./Login.css";
import axios from "axios";
import { BrowserRouter, Switch, Route, Redirect } from "react-router-dom";

class Login extends Component {
  state = {};
  handleSubmit = (e) => {
    e.preventDefault();

    const data = {
      email: this.email,
      password: this.password,
      name: this.firstName,
    };

    axios
      .post("auth/login", data)
      .then((res) => {
        console.log(res);
        localStorage.setItem("token", res.data.token);
        this.setState({
          loggedIn: true,
        });
        this.props.setUser(res.data.user);
      })
      .catch((err) => {
        console.log(err);
        this.setState({
          message: err.response.data.message,
        });
      });
  };
  render() {
    if (this.state.loggedIn) {
      return <Redirect to={"/"} />;
    }
    let error = "";
    if (this.state.message) {
      const cls = "alert alert-" + this.state.cls;
      error = (
        <div className={cls} role="alert">
          {this.state.message}
        </div>
      );
    }
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          {error}
          <h3>Login </h3>
          <div className="form-group">
            <label>Name</label>
            <input
              type="text"
              className="form-control"
              placeholder="First Name"
              onChange={(e) => (this.firstName = e.target.value)}
            />
          </div>

          <div className="form-group">
            <label>Email</label>
            <input
              type="text"
              className="form-control"
              placeholder="Email"
              onChange={(e) => (this.email = e.target.value)}
            />
          </div>
          <div className="form-group">
            <label>Password</label>
            <input
              type="text"
              className="form-control"
              placeholder="Password"
              onChange={(e) => (this.password = e.target.value)}
            />
          </div>

          <button
            type="submit"
            className="btn btn-primary btn-block"
            style={{ background: "black" }}
          >
            Sign up
          </button>
        </form>
      </div>
    );
  }
}

export default Login;
