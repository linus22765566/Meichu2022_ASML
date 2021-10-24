<template>
  <div class="form">
    <img alt="Vue logo" src="../assets/NYCU.jpg" class="mb-3">
    <Formla v-bind:User="User" v-bind:profile="profile"/>
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

</style>