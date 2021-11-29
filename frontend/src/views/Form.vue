<template>
  <div class="container" fluid>
    <div id="nav">
     
      <router-link to="/">Home</router-link> |
      <router-link to="/about">關於這個App</router-link> |
      <router-link to="/formla">我想送食物</router-link>
    </div>
  <div class="form">
    <img alt="Vue logo" src="../assets/NYCU.jpg" class="mb-3">
    <Formla v-bind:User="User" v-bind:profile="profile"/>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Formla from '@/components/Formla.vue'
import liff from '@line/liff';
export default {
  name: 'Form',
  components: {
    Formla
  },
  data(){
      return{
          User:"",
          profile:{}
      };
  },
  beforeCreate(){
      liff
        .init({
            liffId:"1656540074-QGvA1Pdz",withLoginOnExternalBrowser: true,
        })
        .then(()=>{
            this.getProfile();
        })
  },
  methods:{
      getProfile: function(){
          liff
            .getProfile()
            .then((profile) =>{
                this.profile = profile;
                this.User = profile.displayName
            })
            
      }
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