## 一、     安装django
pip install django
## 二、     快速搭建一个blog
1.	在D盘下创建一个pydj的目录  
2.	D:\pydj>django-admin startproject myweb #创建 myweb 项目（使用“startproject”命令来创建项目）
           D:\pydj>cd myweb #进入项目目录
            D:\pydj\myweb>python manage.py startapp blog #创建 blog 应用（使用“startapp”命令创建应用）
 
       3..../myweb/myweb/目录下的 settings.py中39行添加blog应用，添加到第40行 ：‘blog’，
## 三、     admin后台
1.	首先同步数据库  D:\pydj\myweb>python manage.py migrate
2.	创建一个能够登录管理站的用户
D:\pydj\myweb>python manage.py createsuperuser
Username (leave blank to use 'shanqingmei'): shanqingmei #输入登录用户名
Email address: shan_5210@126.com #输入用户邮箱
Password: shanqingmei5210#输入登录密码
Password (again): shanqingmei5210#再次输入用户密码
## 四、     启动服务器
1.	D:\pydj\myweb>python manage.py runserver # 运行 server 服务
2.	通过浏览器访问：http://127.0.0.1:8000/
3.	接着访问 admin 后台：http://127.0.0.1:8000/admin
## 五、     创建blog模型
1.	打开 myweb/blog/models.py 文件，编写如下代码
	
		from __future__ import unicode_literals
		from django.db import models
		from django.contrib import admin

		# Create your models here.
		class Blog(models.Model):
    		title = models.CharField(max_length=150)
    		body = models.TextField()
    		timestamp = models.DateTimeField()

		class BlogAdmin(admin.ModelAdmin):
    		list_display = ('title', 'timestamp')

		admin.site.register(Blog, BlogAdmin)
1.	表名为 Blog，字段分别为 title（char 类型，最长 150 个字符），body（text文本类型）和 timestamp（datetime 日期时间类型）
2.	创建对应的数据库表，执行以下命令：D:\pydj\myweb>python manage.py makemigrations blog
3.	在执行完数据库的创建后，需要重新执行“migrate”命令
        D:\pydj\myweb>python manage.py migrate

## 六、     将blog展示到网页上
1.	创建blog的公共部分
从Django的角度看，一个页面具有三个典型的组件：
一个模板（template）：模板负责把传递进来的信息显示出来。
一个视图（view）：视图负责从数据库获取需要显示的信息。
一个URL模式：它负责把收到的请求和你的试图函数匹配，有时候也会向视图传递一些参数。
2.	创建模板，在../myweb/blog/目录下创建 templates 目录，该目录用来存放 web 页面，在 templates 目录下创建index.html 文件
3.	编写视图

		<!DOCTYPE html>
		<html lang="en">
		<head>
    		<meta charset="UTF-8">
    		<title></title>
		</head>
		<body>
		{% for blog in blogs %}
  			<h2>{{ blog.title }}</h2>
  			<p>{{ blog.timestamp }}</p>
  			<p>{{ blog.body }}</p>
		{% endfor %}
		</body>
		</html>

4.打开.../myweb/blog/views.py 文件

		from django.shortcuts import render
		from blog.models import Blog
		from django.shortcuts import render_to_response

		# Create your views here.
		def index(request):
    		blog_list = Blog.objects.all()
    		return render_to_response('index.html',{'blogs':blog_list})
通过 Blog.objects.all()得到 blog 表中的所有数据，并赋值给 blog\_list 变量。最终将 blog\_list 发送到 index.html 页面

5.配置url

打开.../myweb/myweb/urls.py

		from django.conf.urls import url
		from django.contrib import admin
			urlpatterns = [
	    		url(r'^admin/', admin.site.urls),
    			url(r'^index/$', 'blog.views.index'),
				]
1.	浏览器访问：http://127.0.0.1:8000/index/
2.	到此，我们的 blog 已经搭建完成

## 七、     给blog加点样式

1.	创建基础模板
在.../myweb/blog/templates 目录里创建 base.html 的模板：


		<!DOCTYPE html>
		<html lang="en">
		<head>
    	<meta charset="UTF-8">
    	<style type="text/css">
        	body{color:#0A0A0A;background:#FAFAFA;padding:0 5em;margin:0}
        	h1{padding:2em 1em;background:#7171C6}
        	h2{color:#8B1A1A;border-top:1px dotted #8B2500;margin-top:2em}
        	p{margin:1em 0}
		</style>
		</head>
		<body>
		<h1>Shan blog</h1>
			{% block content %}
			{% endblock %}
		</body>
		</html>
2.	修改index.html模板，让它引用base.html模板

		{% extends "base.html" %}
		{% block content %}
    		{% for blog in blogs %}
        		<h2>{{ blog.title }}</h2>
        		<p>{{ blog.timestamp }}</p>
        		<p>{{ blog.body }}</p>
    		{% endfor %}
		{% endblock %}
刷新链接http://127.0.0.1:8000/index/
# Django 
