<template>
  <div class="container" fluid>
    <div id="nav">
     
      <router-link to="/">Home</router-link> |
      <router-link to="/about">關於這個App</router-link> |
      <router-link to="/formla">我想送食物</router-link>
    </div>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="我們是梅竹黑客松的團隊山東包子!"/>
    
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>

<style scoped lang="scss">
img {
    width: 200px;
    height: 110px;
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