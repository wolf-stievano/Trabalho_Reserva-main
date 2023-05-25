<!-- src/components/RegisterForm.vue -->
<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <input type="text" v-model="username" placeholder="Username" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Registrar</button>
    </form>
  </div>
</template>

<script>
import { registerUser } from "../api";

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async register() {
      try {
        const user = {
          username: this.username,
          password: this.password,
        };
        const userId = await registerUser(user); // Armazenar o retorno da chamada
        this.$emit('register-success', userId);  // Emitir o userId no evento
      } catch (error) {
        console.error(error);
        alert('Registro falhou');
      }
    },
  },
};
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Parisienne&display=swap');

body{
  background-color: #DECDA8;
  font-family: 'Great Vibes', cursive; /* Adicione a fonte ao body para aplicá-la a todo o texto do corpo */
}

background{
  width: 430px;
    height: 520px;
    position: absolute;
    transform: translate(-50%,-50%);
    left: 50%;
    top: 50%;
}

div {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  font-family: 'Parisienne', cursive; /* Substitua a fonte anterior pela Great Vibes */
}

h2{
    font-size: 64px;
    font-weight: 500;
    line-height: 42px;
    text-align: center;
    color: #5a060e;
}

form {
  margin-top: 50px;
  height: 250px;
  width: 400px;
  border-radius: 10px;
  padding: 50px 35px;
  background-color: transparent; /* tornar o fundo do formulário transparente */
}


label{
    display: block;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
}

input{
    display: block;
    height: 50px;
    width: 100%;
    background-color: transparent;
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 14px;
    font-weight: 300;
}

::placeholder{
  color: #5a060e;
    font-family: 'Parisienne', cursive;
    font-size: 20px;
    font-weight: 600;
}

button{
    font-family: 'Parisienne', cursive; /* Substitua a fonte anterior pela Great Vibes */
    margin-top: 50px;
    width: 100%;
    color: #5a060e;
    padding: 10px 0;
    font-size: 40px;
    font-weight: 500;
    border-radius: 3px;
    cursor: pointer;
    background-color: transparent;
}

button:hover {
  background-color:#DAC7A3;
}

/* Adicione este código em ambos os arquivos CSS */

@media screen and (max-width: 768px) {
  form {
    width: 90%;
    padding: 30px 15px;
  }

  h2{
    font-size: 48px;
  }

  input{
    height: 40px;
  }

  button{
    font-size: 30px;
  }
}

</style>


