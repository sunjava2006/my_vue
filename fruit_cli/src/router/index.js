import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/components/login/Login'
import Type from '@/components/type/Type'
import Fruit from '@/components/fruit/Fruit'
import Main from '@/components/main/Main'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
       path: '/main',
       name: 'Main',
       component: Main,
       children:[
        {
          path: '/main/type',
          name: 'Type',
          component: Type
        },
        {
          path: '/main/fruit',
          name: 'Fruit',
          component: Fruit
        }
       ]
    }

  ]
})
