<template>
  <div class="container">
    <!-- 导航栏 -->
    <nav
      
      class="navbar navbar-expand-lg fixed-top navbar-dark bg-secondary"
    >
      <a class="navbar-brand">
        <span class="glyphicon glyphicon-home"></span>
      </a>
      <button
        class="navbar-toggler"
        data-target="#my-nav"
        data-toggle="collapse"
        aria-controls="my-nav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div id="my-nav" class="collapse navbar-collapse">
        <ul class="navbar-nav mr-auto">
          <li
            :class="{ 'nav-item': true, active: currentNavItem == 1 }"
            @click="setCurrItem"
            id="1"
          >
            <!-- 路由到分类管理 -->
            <router-link to="Type" class="nav-link"
              ><span class="glyphicon glyphicon-sort-by-alphabet"></span
              >分类管理</router-link
            >
          </li>
          <li
            :class="{ 'nav-item': true, active: currentNavItem == 2 }"
            @click="setCurrItem"
            id="2"
          >
            <!-- 路由到水果维护 -->
            <router-link to="Fruit" class="nav-link"
              ><span class="glyphicon glyphicon-apple"></span
              >水果维护</router-link
            >
          </li>
        </ul>
        <ul class="navbar-nav navbar-right">
          <li
            :class="{ 'nav-item': true, active: currentNavItem == 3 }"
            @click="setCurrItem"
            id="3"
          >
            <!-- 路由到分类管理 -->
            <a @click="logout" class="nav-link" style="cursor:pointer"
              ><span class="glyphicon glyphicon-log-out"></span>退出</a
            >
          </li>
        </ul>
      </div>
    </nav>
    <router-view ></router-view>
  </div>
</template>

<script>
export default {
    data(){
      return{
        userInfo: null,
        currentNavItem : 1
      }
    },
    
    methods:{
      setCurrItem(e){
        this.currentNavItem = e.currentTarget.id;
      },
      logout(){
        console.log("-----------------logout----------");
        this.axios.get("/logout")
        .then(res => {
          console.log(res)
          if(res.data.logout=='ok'){
            window.sessionStorage.clear();
            this.userInfo=null;
            this.$router.replace('/');
          }
        })
        .catch(err => {
          console.error(err); 
        })
      }
    },
    created(){
      let userInfo = window.sessionStorage.getItem("userInfo")
      this.userInfo = userInfo
      // alert(userInfo)
    //   this.$router.push("/main/type");
    }
};
</script>

<style>
</style>