import React, { useEffect, useState } from "react";
import { getTrips } from "../services/api";

const Trips = () => {
    const [trips, setTrips] = useState([]);

    useEffect(() => {
        getTrips()
            .then((res) => setTrips(res.data))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div>
            <h2>Your Trips</h2>
            {trips.map((trip) => (
                <div key={trip.id}>{trip.name}</div>
            ))}
        </div>
    );
};

export default Trips;
