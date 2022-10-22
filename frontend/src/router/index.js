import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Form from '../views/Form.vue'
import Report from '../views/Report.vue'
// import { createRouter, createWebHistory } from "vue-router";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: '首頁'
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
    meta: {
      title: '關於app'
    }
  },
  {
    path: '/formla',
    name: 'Form',
    component: Form,
    meta: {
      title: '上傳圖片'
    }
  },
  {
    path: '/report',
    name: 'Report',
    component: Report,
    meta: {
      title: '報告'
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


export default router
