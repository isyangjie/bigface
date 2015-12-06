# -*- coding: utf-8 -*-
#该类是用来为“用户”读取或写软件配置文件提供统一的标准接口
#版本: v0.1
#作者: 杨杰
#上次修改时间:2013/11/21

#导入基本模块
import os
import sys
import os.path
import errno

#ConfigManager类的实现

class ConfigManager:
    def __init__(self,ConfigFile,IsCreateFile=True):
        self.ConfigFile=ConfigFile
        #下面的部份不一定有用
        if os.path.exists(os.path.dirname(self.ConfigFile)):
            self.IsUseable=True
        else:
            self.IsUseable=False
        #默认当该配置文件不存在时，创建该配置文件
        if self.IsUseable and IsCreateFile and not os.path.isfile(self.ConfigFile):
            open(self.ConfigFile,'w').close()
        
    #读取配置文件中关键词为Key的键值
    def GetKeyValue(self,Key):
        if Key==None or Key=="":
            return None
                
        if os.path.isfile(self.ConfigFile):
            for line in open(self.ConfigFile,'r'):
                #line.rstrip()
                line_parts=line.split('=')
                if len(line_parts)>0 and line_parts[0]==Key:
                    return line_parts[1].rstrip()
        #文件不存在或该关键值项不存在
        return None
    #向配置文件中添加关键值项
    def AddKeyValue(self,Key,Value):
        if Key==None or Key=="":
            return False

        #先判断该配置文件是否存在
        if os.path.isfile(self.ConfigFile):
            file_read=open(self.ConfigFile,'r')
            for line in file_read:
                #line.rstrip()
                parts=line.split('=')
                if len(parts)>0 and parts[0]==Key:
                    file_read.close()
                    return False
            file_read.close()
            file_write=open(self.ConfigFile,'a')
            LineValue=Key+"="+Value+"\n"
            file_write.write(LineValue)
            file_write.close()
            return True
        else:
            return False
    #设置配置文件中键值为Key的项的值为Value
    def SetKeyValue(self,Key,Value):
        if Key==None or Key=="":
            return False

        IsChange=False#标识参数是否设置成功||状态变量
        if os.path.isfile(self.ConfigFile):
            file_read=open(self.ConfigFile,'r')
            Config=file_read.readlines()
            for i in range(0,len(Config)):
                sub_Config=Config[i]
                #sub_Config.rstrip()
                parts=sub_Config.split('=')
                if len(parts)>0 and parts[0]==Key:
                    Config[i]=Key+"="+Value+"\n"
                    IsChange=True
            file_read.close()
            if IsChange:
                #os.remove(self.ConfigFile)#该行也可以注释掉
                file_write=open(self.ConfigFile,'w')
                file_write.writelines(Config)
                file_write.close()
                return True
            
        return IsChange
    #删除键值为Key的记录
    def DeleteKeyValue(self,Key):
        if Key==None or Key=="":
            return False

        IsDelOk=False
        if os.path.isfile(self.ConfigFile):
            file_read=open(self.ConfigFile,'r')
            Config=file_read.readlines()
            file_read.close()
            for line in Config:
                parts=line.split('=')
                if len(parts)>0:
                    if parts[0]==Key:
                        IsDelOk=True
                        Config.remove(line)

            if IsDelOk:
                file_write=open(self.ConfigFile,'w')
                file_write.writelines(Config)
                file_write.close()

        return IsDelOk

def main():
    MyConfig=ConfigManager("C:\\Users\\xbz\\Desktop\\234.txt")
    MyConfig.AddKeyValue("name","yangjie")
    MyConfig.AddKeyValue("FireWall_Set","True")
    MyConfig.AddKeyValue("sex","men")
    MyConfig.AddKeyValue("FireWall_Set","True")
    MyConfig.AddKeyValue("age","56")
    MyConfig.AddKeyValue("FireWall_Set","True")
    MyConfig.AddKeyValue("girlfriends","marry")
    MyConfig.AddKeyValue("FireWall_Set","True")
    print(MyConfig.GetKeyValue("FireWall_Set"))
    MyConfig.SetKeyValue("FireWall_Set","s")
    print(MyConfig.GetKeyValue("age"))
    MyConfig.DeleteKeyValue("age")
    
    
if __name__=="__main__":
    main()
