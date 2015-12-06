# -*- coding: utf-8 -*-
import web
import os,sys
from web import form
from ConfigManager import ConfigManager


urls=('/WebAuth','WebAuth',
      '/login','login',
      '/register','register',
      '/appscan','appscan',
      '/appgrant','appgrant')

app=web.application(urls,globals())

class login:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        return self.render.login()

class register:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        #self.register_form = form.Form()

    def GET(self):
        return self.render.register()
    
    def POST(self):
        userinfo=web.input()
        realname = userinfo.realname
        telephonenum = userinfo.telephonenum
        emailaddr = userinfo.emailaddr
        SFZ = userinfo.SFZ
        username = userinfo.username
        password = userinfo.password
        password_confirm = userinfo.password_confirm
        sex = usrinfo.optionsRadios
        #write userinfo to database
        return self.render.login()


class appscan(object):
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        return self.render.appscan()


class appgrant(object):
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        cm=ConfigManager('login.conf')
        cm.SetKeyValue("grant","true")
        #data = web.input()
        #GrantToken = data.grantToken
        #web.redirect("http://bigface-test-isyangjie.myalauda.cn/home?username=张三&sex=男&email=zhangsan@sina.com&phone=18781835379&local=中国郑州")
        return self.render.grantsuccessed()

class WebAuth:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
    def GET(self):
        #Handle the input params
        data = web.input()
        cm=ConfigManager('login.conf')
        grant=cm.GetKeyValue("grant")
        if data:
            apptoken = data.appid
            appkey = data.appsecret
            appredirurl = data.redirurl
        else:
            if grant=="true":
                cm.SetKeyValue("grant","false")
                web.seeother("http://bigface-test-isyangjie.myalauda.cn/home?username=张三&sex=男&email=zhangsan@sina.com&phone=18781835379&local=中国郑州")
                return
            else:
                return
        return self.render.service_auth(apptoken)

if __name__=="__main__":
    app.run()
