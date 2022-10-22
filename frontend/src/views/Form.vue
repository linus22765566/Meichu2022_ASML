<template>
  <div class="container" fluid>
    <div id="nav">
      <router-link to="/">首頁</router-link> |
      <router-link to="/formla">upload image</router-link> |
      <router-link to="/report">report</router-link>
    </div>
    <div class="form">
      <img
        src="https://www.geberconsulting.com/images/2018/07/11/clients-logo-size_-1-32.jpg"
      />

      <Formla v-bind:User="User" v-bind:profile="profile" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Formla from '@/components/Formla.vue'

export default {
  name: 'Form',
  components: {
    Formla
  },
  data() {
    return {
      User: '',
      profile: {}
    }
  },
  methods: {}
}
</script>

<style scoped lang="scss">
img {
  width: 400px;
  height: 270px;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>