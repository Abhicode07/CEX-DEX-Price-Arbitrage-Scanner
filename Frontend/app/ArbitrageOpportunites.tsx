import React, { useEffect, useState } from "react";
import axios from "axios";

const ArbitrageOpportunities = () => {
    const [opportunities, setOpportunities] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchOpportunities = async () => {
            try {
                const response = await axios.get("http://127.0.0.1:8000/arbitrage");
                setOpportunities(response.data);
            } catch (error) {
                console.error("Error fetching arbitrage opportunities:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchOpportunities();
    }, []);

    return (
        <div style={{ padding: "20px" }}>
            <h1>Arbitrage Opportunities</h1>
            {loading ? (
                <p>Loading...</p>
            ) : opportunities.length > 0 ? (
                <table>
                    <thead>
                        <tr>
                            <th>Token</th>
                            <th>Binance Price</th>
                            <th>Solana Price</th>
                            <th>Profit</th>
                        </tr>
                    </thead>
                    <tbody>
                        {opportunities.map((opp:any) => (
                            <tr key={opp.token}>
                                <td>{opp.token}</td>
                                <td>{opp.binance_price.toFixed(2)}</td>
                                <td>{opp.solana_price.toFixed(2)}</td>
                                <td>{opp.profit.toFixed(2)}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            ) : (
                <p>No opportunities found.</p>
            )}
        </div>
    );
};

export default ArbitrageOpportunities;
