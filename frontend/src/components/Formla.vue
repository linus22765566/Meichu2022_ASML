<template>
  <form class="formla">
    <h4>
      Hello! {{ User }} Please your design diagram & image with defect <br />
    </h4>

    <div class="mb-3 mx-5">
      <label for="email" class="form-label">Your email</label>
      <input type="email" class="form-control" id="" v-model="email" />
    </div>

    <div class="row">
      <div class="mb-3 mx-5 col">
        <label for="image" class="form-label mx-3">Your golden image</label>

        <input type="file" accept="image/*" @change="previewImage($event, 2)" />
        <template v-if="preview_golden">
          <img :src="preview_golden" height="250px" width="300px" />
        </template>
      </div>
      <div class="col mb-3 mx-5">
        <label for="image" class="form-label">Your defect image</label>

        <input type="file" accept="image/*" @change="previewImage($event, 1)" />
        <template v-if="preview_origin">
          <img :src="preview_origin" height="250px" width="300px" />
        </template>
      </div>
    </div>

    <div class="mb-3 mx-5">
      <label class="form-label">備註</label>
      <input class="form-control" v-model="comment" />
    </div>

    <!-- Button trigger modal -->
    <button
      type="button"
      class="btn btn-primary mb-3"
      data-bs-toggle="modal"
      data-bs-target="#exampleModal"
    >
      送出
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
              You're going to upload this image：
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
              <p align="left">
                圖片：<img
                  :src="preview_origin"
                  class="mb-3"
                  height="250px"
                  width="300px"
                />
              </p>
              <p>(Please wait few seconds for the uploading)</p>
            </div>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>

            <button type="button" class="btn btn-primary" v-on:click="submit">
              Yes
            </button>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>
<script >
import axios from 'axios'
//import { URL } from "url"

import '../assets/index.scss'
export default {
  name: 'Formla',
  props: {
    User: String,
    profile: Object
  },
  data() {
    return {
      Name: '',
      email: '',
      time: '',
      serves: null,
      Maxtake: null,
      comment: '',
      image: null,
      link: '',
      preview_origin: null,
      preview_golden: null
    }
  },

  methods: {
    previewImage: function (event, flag) {
      var input = event.target
      if (input.files) {
        var reader = new FileReader()

        reader.onload = (e) => {
          if (flag == 1) {
            this.preview_origin = e.target.result
          } else {
            this.preview_golden = e.target.result
          }
        }

        reader.readAsDataURL(input.files[0])
      }
    },

    submit: function () {
      var base64_origin = this.preview_origin.split(',')[1]
      var base64_golden = this.preview_golden.split(',')[1]

      console.log(this.preview_origin)
      axios({
        method: 'POST',
        url: 'http://localhost:5000/uploadImage/',

        data: {
          num1: 111,
          origin_image: base64_origin,
          golden_image: base64_golden
        }
      }).then((res) => {
        console.log(res)
        //this.$router.push({ path: 'report' })
      })
    }
  }
}
</script>