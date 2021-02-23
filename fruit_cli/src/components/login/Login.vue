<template>
  <div class="container">
    
      <div class="card ">
        <div class="card-header bg-info text-white ">
          <h3> 管理员登录</h3></div>
        <div class="card-body">
        <div class="input-group">
            <div class="input-group-prepend">
            <span class="input-group-text">登录名</span>
            </div>
            <input class="form-control" type="text" v-model="userName"/>
        </div>
        <br>
        <div class="input-group">
            <div class="input-group-prepend">
            <span class="input-group-text">密码</span>
            </div>
            <input class="form-control" type="password" v-model="pwd"/>
        </div>
        </div>
        <div class="card-footer">{{loginInfo}}
        <button
            class="btn btn-info offset-md-10 offset-lg-11 offset-sm-10 offset-10"
            type="button" v-on:click="login" >
            登录
        </button>
        </div>
    </div>
  </div>
  
</template>

<script>
export default {
  name: "Login",
  
  data() {
    return {
      userName: 'jkwangrui@126.com',
      pwd: '112233',
      loginInfo: null
      // userInfo: null
    };
  },
  methods:{
    login(){
      // alert(this.userName+this.pwd);
      this.axios.get('/login',{params:{userName: this.userName, pwd: this.pwd}})
      .then(res => {
        console.log(res)
        if(res.data.login=='ok'){
          this.userInfo = res.data.userInfo;
          window.sessionStorage.setItem("userInfo", this.userInfo);
      
          console.log(this);
          this.$router.replace('/main/type')

        }else{
          this.loginInfo="用户名或密码不正确"
        }
      })
      .catch(err => {
        console.error(err); 
      })
    }
  }
};
</script>

