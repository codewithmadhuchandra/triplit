import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000/api",
});
const BASE_URL = "http://127.0.0.1:8000/api/";

export async function fetchData() {
    const response = await fetch(`${BASE_URL}your-endpoint/`);
    return response.json();
}

export const getTrips = () => API.get("/trips/");
export const addTrip = (tripData) => API.post("/trips/", tripData);
export const addExpense = (expenseData) => API.post("/expenses/", expenseData);
export const getExpenses = () => API.get("/expenses/");