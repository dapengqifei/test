<template>
  <div class="row">
      <!-- 左右两屏 -->
    <div class="col-md-4">
      <!-- 左边是编辑部分 -->
      <div class="form-group">
          <input type="hidden" v-model="url">
      </div>
      <div class="form-group">
          <input type="text" v-model="title" class="form-control" placeholder="标题">
      </div>
      <div class="form-group">
          <textarea class="form-control" v-model="content" placeholder="内容"></textarea>
      </div>
      <div class="form-group">
          <button class='btn btn-block btn-success' @click="saveBlog()">保存</button>
      </div>

    </div>
    <div class="col-md-8">
      <!-- 右边是博客内容表格部分 -->
      <table class="table table-bordered table-hover">
        <thead>
          <th class="text-center">标题</th>
          <th class="text-center">内容</th>
          <th class="text-center">编辑</th>
          <th class="text-center">删除</th>
        </thead>
        <tbody>
          <tr v-for='blog in blogs' :key='blog.url' >
            <td>{{blog.title}}</td>
            <td>{{blog.content}}</td>
            <td>
              <button class="btn btn-success" @click='editBlog(blog)'>
                <i class="fa fa-edit"></i>
              </button>
            </td>
            <td>
               <button class="btn btn-success" @click='deleteBlog(blog)'>
                <i class="fa fa-trash"></i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Container',
  props: {
  },
  data(){
    return{
      base_url:'http://127.0.0.1:8000/api/blog/',
      blogs:null,
      url:'',
      title:'',
      content:'',
      status:'',
      txt:'22'
    }
  },
  methods:{
    getAll(){
      axios.get(this.base_url)
        .then(res=>{
          this.blogs = res.data;
          this.url = '';
          this.title = ''
          this.content = ''
        });

    },
    demo(){
      axios.get(this.base_url)
          .then(res=>{
            this.blogs = res.data;
            this.status = res.status;
      });

    },
    saveBlog(){
      // 两种情况，一种是新建博客，一种是修改博客,
      // 通过 url是否为空来判断
      if(this.url == ''){
        // 新增
        axios.post(this.base_url,{title:this.title, content:this.content,txt:this.txt})
          .then(()=>{
            this.getAll();
          })
      }else{
        //修改 因为要修改的url已经配置好了
        axios.put(this.url, {title:this.title, content:this.content} )
          .then(()=>{
            this.getAll();
          })
      }

    },
    editBlog(blog){
      this.url = blog.url;
      this.title = blog.title;
      this.content = blog.content;
    },
    deleteBlog(blog){
      axios.delete(blog.url)
        .then(()=>{
            this.getAll();
        });
    }
  },
  created(){
    this.getAll();
  }
}
</script>

<style scoped>

</style>
