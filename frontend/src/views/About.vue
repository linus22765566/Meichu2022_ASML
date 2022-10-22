<template>
  <div class="container" fluid>
    <div id="nav">
      <router-link to="/">首頁</router-link> |
      <router-link to="/about">相關資訊</router-link> |
      <router-link to="/formla">upload image</router-link>
    </div>
    <div class="about">
      <h1>這是一個可以上傳defect image, 進行compare & report 的平台</h1>
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
