<template>
  <div class="container">
    <div class="card">
      <div class="card-header">添加水果分类</div>
      <div class="card-body">
        <div class="input-group">
          <div class="input-group-prepend">
            <span class="input-group-text">分类名</span>
          </div>
          <input class="form-control" type="text" v-model="type" />
          <div class="input-group-append">
            <button class="btn btn-secondary">添加</button>
          </div>
        </div>
      </div>
      <!-- <div class="card-footer">Footer</div> -->
    </div>
    <!-- end card -->
    <br />
    <table class="table table-light table-striped">
      <thead class="thead-light">
        <tr>
          <th>序号</th>
          <th>类型名</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in typeList" :key="index">
          <td>{{ item.RO }}</td>
          <td>{{ item.TYPE }}</td>
          <td>
            <div
              class="btn-group offset-7 offset-sm-4"
              role="group"
              aria-label="Button group"
            >
              <button class="btn btn-secondary">修改</button>
              <button class="btn btn-secondary">删除</button>
            </div>
  
          </td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th colspan="2">
            总{{ totalCount }}条记录，共{{ totalPage }}页，当前第{{
              currentPage
            }}页.
          </th>
          <th>
            <div
              class="btn-group offset-6 offset-sm-4"
              role="group"
              aria-label="Button group"
            >
              <button v-if="currentPage>1" class="btn btn-secondary" v-on:click="previousPage" >上一页</button>
              <button v-if="currentPage<totalPage" class="btn btn-secondary" v-on:click="nextPage" >下一页</button>
            </div>
          </th>
        </tr>
      </tfoot>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      type: null,
      typeList: null,
      currentPage: 1,
      size: 3,
      totalCount: 0,
      totalPage: 1,
    };
  },
  methods: {
    nextPage(){
      this.listType(this.currentPage+1, this.size);
    },
    previousPage(){
      this.listType(this.currentPage-1, this.size);
    },
    listType(page, size){
      this.axios
      .get("/listTypes", { params: { page: page, size: size } })
      .then((res) => {
        console.log(res);
        this.typeList = res.data.typeList;
        this.totalCount = res.data.totalCount;
        this.totalPage = res.data.totalPage;
        this.currentPage = res.data.currentPage;
      })
      .catch((err) => {
        console.error(err);
      });
    }
  },
  created() {
    this.listType(1, this.size);
  },
};
</script>

<style>
</style>

