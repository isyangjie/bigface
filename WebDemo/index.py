# -*- coding: utf-8 -*-
import web
import os,sys

urls=('/login','index',
      '/home','home')

app=web.application(urls,globals())

class index:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.app_id = "59748b45bf3437496f20ff6fd4cde3b0"
        self.app_secret = "69729b45bf3448499f20ff6fd4c5e3b0"
        self.redir_url = "http://127.0.0.1:8888/user"
    def GET(self):
        #Init bigface login params
        return self.render.index(self.app_id,self.app_secret,self.redir_url)


class home:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)


    def GET(self):
        data = web.input()
        username = data.username
        sex = data.sex
        email = data.email
        phone = data.phone
        local = data.local
        return self.render.home(username,sex,email,phone,local)

if __name__=="__main__":
    app.run()
