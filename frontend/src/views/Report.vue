<template>
  <div class="container" fluid>
    <div id="nav">
      <router-link to="/">首頁</router-link> |
      <router-link to="/formla">upload image</router-link> |
      <router-link to="/report">report</router-link>
    </div>

    <div class="container">
      <p>x</p>
      <span class="row">
        <div class="col d-flex align-items-center" v-if="this.num_left > 0">
          <span style="width: 70px" class="small" id="inputGroup-sizing-sm"
            >我要領取</span
          >
          <input
            type="text"
            style="width: 50px"
            class="form-control"
            aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-sm"
            v-model="amount"
            border-color="#ccc"
          />

          <span style="width: 40px" class="small" id="inputGroup-sizing-sm">
            個</span
          >
        </div>

        <div class="col">
          <div
            class="alert alert-danger"
            role="alert"
            v-if="this.amount > this.Maxtake"
          >
            不可以領超過上限!!!
          </div>
          <!-- Button trigger modal -->
          <button
            type="button"
            class="btn btn-primary mb-3"
            data-bs-toggle="modal"
            v-if="this.num_left > 0 && this.amount <= this.Maxtake"
            data-bs-target="#exampleModal"
          >
            送出表單
          </button>

          <!-- Modal -->
          <div
            class="modal fade"
            id="exampleModal"
            tabindex="-1"
            aria-labelledby="exampleModalLabel"
            aria-hidden="true"
          >
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLabel">
                    以下為你訂購的資訊：
                  </h5>
                  <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                  ></button>
                </div>
                <div class="modal-body">
                  <div>
                    <h1 align="left">{{ foodName }}</h1>
                    <p align="left">領取地點：{{ location }}</p>
                    <p align="left">最晚領取時間：{{ time }}</p>
                    <p align="left">你登記了：{{ amount }}個</p>
                  </div>
                </div>
                <div class="modal-footer">
                  <button
                    type="button"
                    class="btn btn-primary"
                    v-on:click="submit"
                  >
                    確認
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </span>
    </div>
  </div>
</template>

<script>
// import { defineComponent } from '@vue/composition-api'
import axios from 'axios'

export default {
  // props:{
  //     name:String,
  //     item:String,
  //     location:String,
  //     time:String,
  //     left:Number,
  //     max:Number,
  //     comment
  // },
  data() {
    return {
      User: '',
      uid: '',
      foodName: '',
      location: '',
      time: '',
      num_left: null,
      Maxtake: null,
      comment: '',
      amount: ''
    }
  },
  beforeCreate() {
    var getUrlString = location.href.split('/')

    //this.uid = getUrlString[getUrlString.LastIndexOf('/')]
    this.uid = getUrlString[getUrlString.length - 1]

    axios
      .get('https://a6be-140-113-124-40.ngrok.io/getDetail', {
        params: {
          id: this.uid
        }
      })
      .then((response) => {
        console.log(response.data)
        this.foodName = response.data[0]['item']
        this.location = response.data[0]['location']
        this.time = response.data[0]['time']
        this.num_left = response.data[0]['left']
        this.Maxtake = response.data[0]['max']
      })
      .catch((error) => console.log(error))
  },
  methods: {
    show: function () {
      console.log(this.uid)
      console.log(this.amount)
    },
    submit: function () {
      //var getUrlString = location.href;
      axios
        .post('https://a6be-140-113-124-40.ngrok.io/reserve', {
          id: location.href[location.href.length - 1],
          amount: this.amount
        })
        .then((response) => {
          console.log(response)
          window.location.reload()
        })
        .catch((error) => console.log(error))
    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.mx {
  margin-left: 50px;
  margin-right: 0px;
}
</style>

