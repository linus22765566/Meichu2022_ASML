<template>
  <div class="container" fluid>
    <div id="nav">
      <router-link to="/">首頁</router-link> |
      <router-link to="/formla">upload image</router-link> |
      <router-link to="/report">report</router-link>
    </div>
    <div class="home">
      <img
        class="mb-3"
        src="https://inside-assets1.inside.com.tw/2020/12/kq10py4yek33hsjg7mz4ulkq3z03t9.jpg?auto=compress&fit=crop&h=675&w=1200"
      />
      <HelloWorld msg="我們是梅竹黑客松的交大資工宇宙戰艦!" />
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
  width: 400px;
  height: 210px;
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
