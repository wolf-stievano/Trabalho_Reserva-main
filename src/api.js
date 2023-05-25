const API_URL = "http://localhost:5000/api";

async function fetchData(url, options) {
  const response = await fetch(url, options);
  if (!response.ok) {
    throw new Error(`Failed to fetch: ${response.status}`);
  }
  return response.json();
}

export async function getReservations(userId) {
  return fetchData(`${API_URL}/reservations/${userId}`);
}

export async function createReservation(reservation, userId) {
  reservation.user_id = userId;
  return fetchData(`${API_URL}/reservations`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(reservation),
  });
}

export async function updateReservation(reservationId, reservation) {
  return fetchData(`${API_URL}/reservations/${reservationId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(reservation),
  });
}

export async function deleteReservation(reservationId) {
  return fetchData(`${API_URL}/reservations/${reservationId}`, {
    method: "DELETE",
  });
}

export async function loginUser(user) {
  const response = await fetchData(`${API_URL}/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  });
  console.log(response);
  return response.user_id;
}

export async function registerUser(user) {
  const response = await fetchData(`${API_URL}/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  });
  return response._id;
}