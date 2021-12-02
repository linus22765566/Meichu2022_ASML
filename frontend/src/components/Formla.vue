<template>
  <form class="formla">
      <h4>hi {{User}} 以下是表單 <br> 填寫完按下送出即可~</h4>
  <div class="mb-2 mx-5">
    <label class="form-label">食物名稱</label>
    <input class="form-control" required v-model="foodName">
  </div>

  <div class="mb-3 mx-5">
    <label for="location" class="form-label">你的所在位置</label>
    <input type="location" class="form-control" required id="location" v-model="location">
  </div>
  <label for="time" class="form-label">你會待到幾點呢?</label>
  <div class="mb-3 mx-5 col">
    <input type="time" class="form-control" required id="time" v-model="time">
    </div>

  <div class="row">

    <div class="ms-5 col">
    <label for="serve" required class="form-label">總共有幾份</label>
    <input type="serve" class="form-control" id="serve" v-model="serves">
    </div>
     <div class="mb-4 me-5 col">
    <label for="maxtake" required class="form-label">一人最多拿幾份</label>
    <select class="form-select" id="maxtake" v-model="Maxtake">
    
    <option value="1">1</option>
    <option value="2">2</option>
    <option value="3">3</option>
    <option value="4">4</option>
    <option value="5">5</option>
    </select>
   </div>
  </div>

   

    <div class="mb-3 mx-5">
    <label for="image" class="form-label mx-3">要附上食物的照片嗎?</label>

    <input type="file" accept="image/*" @change="previewImage($event)">
    <template v-if="preview">
      <img :src="preview" height="250px" width="300px"/>
    </template>
    </div>
 
 
  <div class="mb-3 mx-5">
    <label  class="form-label" >備註</label>
    <input  class="form-control" v-model="comment">
  </div>
  


  <!-- Button trigger modal -->
<button type="button" class="btn btn-primary mb-3" data-bs-toggle="modal" data-bs-target="#exampleModal">
  送出表單
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">以下為表單資訊：</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div>
            
            <h1 align="left" >{{foodName}}</h1>
            <p align="left">領取地點：{{location}}</p>
            <p align="left">最晚領取時間：{{time}}</p>
            <p align="left">總共數量：{{serves}}</p>
            <p align="left">領取上限：{{Maxtake}}</p>
            <p align="left">備註：{{comment}}</p>
            <p align="left">圖片：<img :src="preview" class="mb-3" height="250px" width="300px"/></p>
            <p>(按下送出鈕需要稍微等待一下頁面重整喔~)</p>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">關閉</button>
        <button type="button" class="btn btn-primary" v-on:click="submit">確認並送出</button>
      </div>
    </div>
  </div>
</div>
</form>
</template>
<script >

import axios from "axios"
//import { URL } from "url"




export default {
  name:"Formla",
    props: {
        User: String,
        profile: Object
    },
    data() {
        return {
        Name:"",
        foodName:"",
        location: "",
        time:"",
        serves:null,
        Maxtake:null,
        comment: "",
        image:null,
        link:"",
        preview:null
      }
    },
    methods:{
      previewImage: function(event) {
      var input = event.target;
      if (input.files) {
        //const data = URL.createObjectURL(input.files[0]);
        
        
        var reader = new FileReader();
        reader.onload = (e) => {
          this.preview = e.target.result;
        }
        this.image=input.files[0];
        reader.readAsDataURL(input.files[0])
      }
      
    },
    submit: function(){
      
      var base64 = this.preview.replace(/^data:image\/(png|jpg|jpeg);base64,/, "");
      console.log('111',base64)
      axios({
        method: 'POST',
        url: 'https://api.imgur.com/3/image',
        data: {
          'image':base64
          },
        headers: {
        Authorization: "Client-ID 91f00c5cce32b64"  //放置你剛剛申請的Client-ID
        }})
        .then((res)=>{
        
      console.log(this.link)
      axios.post('https://a6be-140-113-124-40.ngrok.io/addForm',{
      name:res['data'].data.link,
      image:res['data'].data.link,
      item: this.foodName,
      location: this.location,
      time: this.time + ':00',
      left: this.serves,
      max:this. Maxtake,
      comment: this.comment,})
    .then( (response) =>{
      // if(response.data['mes'] == 'add form success')
      // {
      //   console.log('hihi')
      //   console.log(this.profile)
      //   axios.post('https://fake-kp.herokuapp.com/callback',{
      //     id:this.profile['userId'],
      //     user:this.User,
      //     foodname:this.foodName,
      //     location:this.location,
      //     serves:this.serves,
      //     url:response.data['url']
      //   })
      // }
      console.log(response)
       window.location.reload()
    })
    .catch( (error) => console.log(error))
    })
    }
    
    }
}


</script>