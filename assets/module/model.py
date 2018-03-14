import re
import assets.message.MessageManage as Msg
import assets.feature.feature as feature
import assets.module.judge as judge
import assets.feature.filesystem as fs
import assets.Global.Global as Global

class ModuleModel:
    def __init__(self):
        self.locate = fs.FileSystem().getUserlocate()
        self.doPath = None 
        self.check = False
        self.type = "DEFAULT" 
        self.size = "100,100"

    def modelLoop(self):
        try:
            Msg.Message.sucMessage(1)
            
            while 1:
                self.doPath = input("> Enter Address : ({:8}) ".format(self.locate)) # 做例外處理
                self.doPath = judge.Appropriate(self.doPath,self.locate).checkType()
                self.type = input("> Enter Type : (default) ") 
                self.type = judge.Appropriate(self.type,"DEFAULT").checkType()
                
                if self.type.upper().strip() == "DELETE": # delete backup file
                    fs.FileSystem().deleteDirectory()
                    continue

                if self.type.upper().strip() == "COPY": # to backup file and directory
                    fs.FileSystem().buildDirectory()
                elif self.type.upper().strip() == "ANDROID":
                    # do android icon play
                    self.type = input("> Enter run type : (normal) ")
                    self.type = judge.Appropriate(self.type,"NORMAL").checkType()
                    if self.type.upper().strip() == "NORMAL":
                        fs.FileSystem().buildDirectory("Android")
                        for i in range(len(Global.ANDROID_MIPMAP)):
                            fs.FileSystem().buildDirectory("Android/"+Global.ANDROID_MIPMAP[i])
                            feature.Switch().tryTest(self.doPath,Global.ANDROID_MIPMAPSIZE[i],self.type,"Android/"+Global.ANDROID_MIPMAP[i]+"/")
                        Msg.Message.sucMessage(2,"build new diretory \"Android\" in {:10} ".format(self.doPath))
                    elif self.type.upper().strip() == "COPY":
                        # self.type = androidtype # self type = android type 
                        fs.FileSystem().buildDirectory()
                        fs.FileSystem().buildDirectory("Backup/Android/")
                        for i in range(len(Global.ANDROID_MIPMAP)):
                            fs.FileSystem().buildDirectory("Backup/Android/"+Global.ANDROID_MIPMAP[i])
                            feature.Switch().tryTest(self.doPath,Global.ANDROID_MIPMAPSIZE[i],self.type,"Android/"+Global.ANDROID_MIPMAP[i]+"/")
                        Msg.Message.sucMessage(2,"build new diretory \"Android\" in Backup ")

                    continue             
                self.size = input("> Enter Size : (100x100) ")
                self.size = judge.Appropriate(self.size,"100,100").checkType()
                self.size = self.size.replace("(","").replace(")","")
                self.size = tuple(map(int,re.split(",|x|X| ",self.size.strip())))
                # do image deal with 
                feature.Switch().tryTest(self.doPath,self.size,self.type)
                Msg.Message.msgMessage(3,"path: {:10} , type: {:10} , size: {:10}".format(self.doPath,self.type,str(self.size)))

        except:
            Msg.Message.msgMessage(3,"\nfinally!")
            