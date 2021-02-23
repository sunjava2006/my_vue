// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

// 在应用入口注册BootstrapVue 
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
import 'bootstrap/'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// axios
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

// 设置拦截器，对返回的响应头信息进行过滤。发现会话过期，跳转到登录页面。
axios.interceptors.response.use(response => {
  if(response.headers['session-status']=='invalide'){
    console.log("会话已经失效。。。。")
    router.replace("/");
  }
return response;
},error => {
// Do something with response error
return Promise.reject(error);
});


// 设置跨域目标
axios.defaults.baseURL='/api'
// Vue.prototype.HOST = 'http://localhost:8080/api'
// console.log("-------------------------------" + Vue.prototype.HOST)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
