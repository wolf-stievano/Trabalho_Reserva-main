<template>
  <div>
    <h2>Formulário de Reserva de Mesas</h2>
    <form v-if="!isEditing" @submit.prevent="addReservation" class="reservation-form">
      <div>
        <label for="name">Nome:</label>
        <input type="text" id="name" v-model="newReservation.name" placeholder="Digite o nome" required>
      </div>
      <div>
        <label for="date">Data:</label>
        <input type="date" id="date" v-model="newReservation.date" required>
      </div>
      <div>
        <label for="time">Hora:</label>
        <input type="time" id="time" v-model="newReservation.time" required>
      </div>
      <div>
        <label for="guests">Número de Pessoas:</label>
        <input type="number" id="guests" v-model="newReservation.guests" required>
      </div>
      <button type="submit">Enviar</button>
    </form>

    <form v-else @submit.prevent="updateReservation">
      <div>
        <label for="name">Nome:</label>
        <input type="text" id="name" v-model="editingReservation.name" required>
      </div>
      <div>
        <label for="date">Data:</label>
        <input type="date" id="date" v-model="editingReservation.date" required>
      </div>
      <div>
        <label for="time">Hora:</label>
        <input type="time" id="time" v-model="editingReservation.time" required>
      </div>
      <div>
        <label for="guests">Número de Pessoas:</label>
        <input type="number" id="guests" v-model="editingReservation.guests" required>
      </div>
      <button type="submit">Atualizar</button>
      <button @click="cancelEditing">Cancelar</button>
    </form>
    <ul>
      <!-- Dentro do loop v-for -->
<li v-for="reservation in reservations" :key="reservation._id" class="reservation-item">
  <div>
    <button @click="startEditing(reservation)" class="edit-button">Editar</button>
    <button @click="deleteReservation(reservation._id)" class="delete-button">Excluir</button>
  </div>
  <div>
    <span class="reservation-details">{{ reservation.name }}</span>
    <span class="reservation-details">{{ reservation.date }}</span>
    <span class="reservation-details">{{ reservation.time }}</span>
    <span class="reservation-details">{{ reservation.guests }} pessoas</span>
  </div>
</li>

    </ul>
  </div>
</template>

<script>
import { createReservation, getReservations, deleteReservation, updateReservation } from "../api";

export default {
  data() {
    return {
      reservations: [],
      newReservation: {
        name: "",
        date: "",
        time: "",
        guests: "",
      },
      isEditing: false,
      editingReservation: null,
      userId: null,
    };
  },

  methods: {
    async loadReservations(userId) {
      this.userId = userId;
      this.reservations = await getReservations(userId);
    },

  async addReservation() {
    const today = new Date();
    today.setHours(0, 0, 0, 0); // Defina as horas, minutos e segundos para zero para comparar apenas as datas
    const reservationDate = new Date(this.newReservation.date);

    // Verifique se a data da reserva é anterior ao dia atual
    if (reservationDate < today) {
      alert('A data da reserva não pode ser anterior ao dia atual');
      return;
    }

     // Verifique se o número de convidados excede 30
  if (this.newReservation.guests > 30) {
    alert('O número máximo de convidados é 30');
    return;
  }

    //verifique se o numero de convidados é menor que 1
  if (this.newReservation.guests < 1) {
    alert('O número mínimo de convidados é 1');
    return;
  }

    const reservation = {
      name: this.newReservation.name,
      date: this.newReservation.date,
      time: this.newReservation.time,
      guests: this.newReservation.guests,
    };

    const createdReservation = await createReservation(reservation, this.userId);
    this.reservations.push(createdReservation);
    this.newReservation.name = '';
    this.newReservation.date = '';
    this.newReservation.time = '';
    this.newReservation.guests = '';
  },

  async deleteReservation(reservationId) {
      await deleteReservation(reservationId);
      this.reservations = this.reservations.filter((reservation) => reservation._id !== reservationId);
    },

startEditing(reservation) {
this.isEditing = true;
this.editingReservation = { ...reservation };
},

async updateReservation() {
  const today = new Date();
  today.setHours(0, 0, 0, 0); // Defina as horas, minutos e segundos para zero para comparar apenas as datas
  const reservationDate = new Date(this.editingReservation.date);

  // Verifique se a data da reserva é anterior ao dia atual
  if (reservationDate < today) {
    alert('A data da reserva não pode ser anterior ao dia atual');
    return;
  }

  // Verifique se o número de convidados excede 30
  if (this.editingReservation.guests > 30) {
    alert('O número máximo de convidados é 30');
    return;
  }

  // Verifique se o número de convidados é menor que 1
  if (this.editingReservation.guests < 1) {
    alert('O número mínimo de convidados é 1');
    return;
  }

const { _id, ...reservation } = this.editingReservation;
await updateReservation(_id, reservation);
const index = this.reservations.findIndex((r) => r._id === _id);
if (index !== -1) {
this.reservations.splice(index, 1, this.editingReservation);
}
this.cancelEditing();
},
cancelEditing() {
this.isEditing = false;
this.editingReservation = null;
},
clearForm() {
this.newReservation.name = '';
this.newReservation.date = '';
this.newReservation.time = '';
this.newReservation.guests = '';
},

},
};
</script>

<style scoped src="./ReservationForm.css"></style>