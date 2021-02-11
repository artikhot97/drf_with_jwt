import { Component } from "react";
import axios from "axios";

class Home extends Component {
  render() {
    if (this.props.user) {
      return (
        <div>
          {this.props.user.first_name} {this.props.user.last_name}
        </div>
      );
    }
  }
}

export default Home;
