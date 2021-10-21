<template>
  <form class="formla">
      <h4>hi {{User}} {{foodName}} 以下是表單 <br> 填寫完按下送出即可~</h4>
  <div class="mb-2 mx-5">
    <label class="form-label">食物名稱</label>
    <input class="form-control" required v-model="foodName">
  </div>

  <div class="mb-3 mx-5">
    <label for="location" class="form-label">你的所在位置</label>
    <input type="location" class="form-control" id="location">
  </div>
  <label for="time" class="form-label">你會待到幾點呢?</label>
  <div class="mb-3 mx-5 col">
    <input type="time" class="form-control"  id="time">
    </div>
 <div id="timeHelp" class="form-text mb-3">(可以點擊小時鐘,直接選取時間喔!)</div>
  <div class="row">

    <div class="ms-5 col">
    <label for="serve" class="form-label">總共有幾份</label>
    <input type="serve" class="form-control" id="serve">
    </div>
     <div class="mb-4 me-5 col">
    <label for="maxtake" class="form-label">一個人最多拿幾份</label>
    <select class="form-select" id="maxtake">
    
    <option value="1">1</option>
    <option value="2">2</option>
    <option value="3">3</option>
    <option value="4">4</option>
    <option value="5">5</option>
    </select>
   </div>
  </div>

   

    <div class="mb-3 mx-5">
    <label for="image" class="form-label">要附上食物的照片嗎?</label>
    <input type="image" class="form-control" id="image">
    </div>
 
 
  <div class="mb-3 mx-5">
    <label  class="form-label">備註</label>
    <input  class="form-control">
  </div>
  


  <!-- Button trigger modal -->
<button type="button" class="btn btn-primary mb-3" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

</form>
</template>

<script>

// import liff from '@line/liff';
// import { onMounted } from "vue";
    
export default {
  name:"Formla",
    props: {
        User: String,
        profile: Object
    },
    data() {
        return {
        foodName:"",
        location: "",
        time:{
            required: true,
            type:String,   
        },
        serves:{
            type:Number,
            required: true
        },
        Maxtake:{
            type:Number,
            default: 2
        },
        comment: {
            type: String,
            required: true,
        }}
    },
    
}

</script>