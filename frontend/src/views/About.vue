<template>
  <div class="container" fluid>
    <div id="nav">
     
      <router-link to="/">Home</router-link> |
      <router-link to="/about">關於這個App</router-link> |
      <router-link to="/formla">我想送食物</router-link>
    </div>
    <div class="about">
      <h1>這是一個可以讓清交學生<br>在處理營隊/會議多出來的<br>食物時，更方便快速的平台</h1>
    </div>
  </div>
</template>

<style lang="scss">
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