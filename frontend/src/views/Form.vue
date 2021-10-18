<template>
  <div class="form">
    <img alt="Vue logo" src="../assets/NYCU.jpg" class="mb-3">
    <Formla User="Linus"/>
  </div>
</template>

<script>
// @ is an alias to /src

import Formla from '@/components/Formla.vue'

export default {
  name: 'Form',
  components: {
    Formla
  }
}
</script>

<style scoped lang="scss">
img {
    width: 200px;
    height: 110px;
}

</style>