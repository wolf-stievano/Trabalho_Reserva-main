<script setup lang="ts">
</script>

<template>
  <div id="app">
    <main>
      <login-form v-if="!loggedIn && !showRegister" @login-success="loginSuccess" @go-to-register="showRegister = true" />
      <register-form v-if="!loggedIn && showRegister" @register-success="loginSuccess" @go-to-login="showRegister = false" class="register-form"/>
      <div class="reservation-container" v-if="loggedIn">
        <site-blindao ref="siteBlindao" />
      </div>
    </main>
  </div>
</template>


<script>
import LoginForm from "./components/LoginForm.vue";
import RegisterForm from "./components/RegisterForm.vue";
import SiteBlindao from "./components/SiteBlindao.vue";

export default {
  components: {
    LoginForm,
    SiteBlindao,
    RegisterForm,
  },
  data() {
    return {
      loggedIn: false,
      showRegister: false,
    };
  },
  methods: {
    loginSuccess(userId) {
    this.loggedIn = true;
    this.$nextTick(() => {
      this.$refs.siteBlindao.loadReservations(userId);
    });
  },
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Parisienne&display=swap');

body {
  font-family: 'Parisienne', cursive;
  height: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh; /* changed from height to min-height */
  background-image: url('./assets/papel.jpg');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: top;
}

main {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 1rem;
  flex-grow: 1;
  background-color: transparent;
}

</style>



