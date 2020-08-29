# django-vue前后端分离

## 做什么
使用django vue来实现前后端分离的web项目，以博客的CRUD为例子

## 技术栈 
* 后端 backends
  * django
  * django rest framework
  * django cors headers 
* 前端 frontends
  * vue
  * bootstrap 
  * fontawesome

## 步骤
1. 后端
   1. 安装django 我这里已经安装好了 
   2. 创建django项目
   3. 添加博客的Model， 并添加一些初始数据
   4. 使用restframework来添加serializer、viewset、urls
   5. 设置跨域 cors headers
2. 前端
   1. 安装node vue /事先已经配置好了淘宝的镜像 
   2. vue-cli创建前端项目
   3. 修改index.html主页 添加bootstrap css框架和fontawsome字体的依赖
   4. 修改App.vue和核心组件 
   5. 添加axios http请求组件
   6. 添加请求后端代码 