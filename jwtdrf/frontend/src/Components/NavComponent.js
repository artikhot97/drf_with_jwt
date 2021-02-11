import React, { Component } from "react";
import "../App.css";
import "../../node_modules/bootstrap/dist/css/bootstrap.min.css";

import { Link } from "react-router-dom";
class NavComponent extends Component {
  handleLogout = () => {
    localStorage.clear();
    this.props.setUser(null);
  };
  render() {
    let navbarDisplay;
    if (this.props.user) {
      navbarDisplay = (
        <ul className="navbar-nav ml-auto">
          <li className="nav-item">
            <Link
              className="nav-link active"
              aria-current="page"
              to={"/"}
              onClick={this.handleLogout}
            >
              Logout
            </Link>
          </li>
        </ul>
      );
    } else {
      navbarDisplay = (
        <ul className="navbar-nav ml-auto">
          <li className="nav-item">
            <Link className="nav-link active" aria-current="page" to={"/login"}>
              Login
            </Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to={"/register"}>
              Sign up
            </Link>
          </li>
        </ul>
      );
    }
    return (
      <div>
        <nav className="navbar navbar-expand-lg navbar-light fixed-top">
          <div className="container">
            <Link className="navbar-brand" to={"/"}>
              Home
            </Link>
            <div className="collapse navbar-collapse" id="navbarNav">
              {navbarDisplay}
            </div>
          </div>
        </nav>
      </div>
    );
  }
}
export default NavComponent;
