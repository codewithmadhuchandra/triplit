import React, { useEffect, useState } from "react";
import { getExpenses } from "../services/api";

const TripDetails = ({ tripId }) => {
    const [expenses, setExpenses] = useState([]);

    useEffect(() => {
        getExpenses(tripId)
            .then((res) => setExpenses(res.data))
            .catch((err) => console.error(err));
    }, [tripId]);

    return (
        <div>
            <h2>Trip Expenses</h2>
            {expenses.map((expense) => (
                <div key={expense.id}>{expense.description} - ₹{expense.amount}</div>
            ))}
        </div>
    );
};

export default TripDetails;
