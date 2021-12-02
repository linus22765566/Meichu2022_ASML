<template>
    <div class="mx" style="width: 300px;">
        <div>
            <span class="row  mb-3" style="height: 38px margin: 10px">
                <h1 class="mt-3 mb-2" align="center">{{foodName}}</h1>
            </span>
            <div class="container">
                <div class="row">
                    <p align="left">領取地點：{{location}}</p>
                    <p align="left">最晚領取時間：{{time}}</p>
                    <p align="left">一人領取上限：{{Maxtake}}</p>
                    <p align="left">剩餘數量：{{num_left}}</p>
                </div>
            </div>
            
        </div>
        <div class="container">
            <span class="row">
                <div class="col d-flex align-items-center">    
                    <span style="width: 70px" class="small" id="inputGroup-sizing-sm">我要領取</span>
                    <input type="text" style="width: 50px" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" v-model="amount">
                    <span style="width: 40px" class="small" id="inputGroup-sizing-sm"> 個</span>    
                </div>
                <div class="col">
                  
                    <!-- Button trigger modal -->
<button type="button" class="btn btn-primary mb-3" data-bs-toggle="modal" data-bs-target="#exampleModal">
  送出表單
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">以下為你訂購的資訊：</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div>
            
            <h1 align="left" >{{foodName}}</h1>
            <p align="left">領取地點：{{location}}</p>
            <p align="left">最晚領取時間：{{time}}</p>
            <p align="left">你登記了：{{amount}}個</p>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" v-on:click="submit">確認</button>
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
import axios from "axios"


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
    data(){
        return {
        User:"",
        uid:"",
        foodName:"",
        location: "",
        time:"",
        num_left:null,
        Maxtake:null,
        comment:"",
        amount:""
      }
    },
    beforeCreate(){
        var getUrlString = location.href;
        this.uid = getUrlString[getUrlString.indexOf('access_token') -4]
        this.uid = getUrlString[(getUrlString.length)-1]
        
        axios.get('https://a6be-140-113-124-40.ngrok.io/getDetail',{
          params:{
            id:this.uid
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
    methods:{
        show: function(){
            console.log(this.uid)
            console.log(this.amount)
        },
        submit: function(){
            //var getUrlString = location.href;
            axios.post('https://a6be-140-113-124-40.ngrok.io/reserve',{
            id:location.href[(location.href.length)-1],
            amount:this.amount
        })
            .then( (response) => {console.log(response)
                window.location.reload()
            })
            .catch( (error) => console.log(error))
    }
}
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.mx{
    margin-left: 50px;
    margin-right: 0px;
}
</style>

