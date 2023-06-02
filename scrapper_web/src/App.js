import './App.css';
import React, { Component } from "react";
import axios from "axios";

function App() {

  return (
    
    <div className="App">
      <CryptocurrencyTable />
    </div>
  );
}




class CryptocurrencyTable extends Component {
    constructor(props) {
        super(props);

        this.state = {
            cryptocurrencyData: [],
        };
    }

    componentDidMount() {
      // setInterval(() => {
        axios.get("http://127.0.0.1:8000/app/get_data").then((response) => {
            this.setState({
                cryptocurrencyData: JSON.parse(response.data),
            });
            // console.log(JSON.parse(response.data))
        });
      // }, );
    }
    
    
    render() {
      // console.log(this.state.cryptocurrencyData)
        return (
            <table class="styled-table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Price</th>
                        <th>1h%</th>
                        <th>24h%</th>
                        <th>7d%</th>
                        <th>Market Cap</th>
                        <th>volume(24h)</th>
                        <th>Circulating Supply</th>
                    </tr>
                </thead>
                <tbody style ={{height: '100px'}}>
                    {this.state.cryptocurrencyData.map((cryptocurrency) => {  
                      console.log(cryptocurrency.fields)
                      return (
                        <tr style ={{color: 'black'}} key={cryptocurrency.fields.name}>
                            <td>{cryptocurrency.fields.name}</td>
                            <td>{cryptocurrency.fields.price}</td>
                            <td>{cryptocurrency.fields.one_h_percent}</td>
                            <td>{cryptocurrency.fields.twentyFour_h_percent}</td>
                            <td>{cryptocurrency.fields.seven_d_percent}</td>
                            <td>{cryptocurrency.fields.market_cap}</td>
                            <td>{cryptocurrency.fields.volume_24h}</td>
                            <td>{cryptocurrency.fields.circulating_supply}</td>
                        </tr>
                    )})}
                </tbody>
            </table>
        );
    }
}

export default App;

// export default CryptocurrencyTable;
