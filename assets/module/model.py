import re
import assets.message.MessageManage as Msg
import assets.feature.feature as feature
import assets.module.judge as judge
import assets.feature.filesystem as fs

class ModuleModel:
    def __init__(self):
        self.locate = fs.FileSystem().getUserlocate()
        self.doPath = None 
        self.check = False
        self.type = "DEFAULT" 
        self.size = "100,100"

    def modelLoop(self):
        # try:
            Msg.Message.sucMessage(1)
            
            while 1:
                self.doPath = input("> Enter Address : ({:8}) ".format(self.locate)) # 做例外處理
                self.doPath = judge.Appropriate(self.doPath,self.locate).checkType()
                self.type = input("> Enter Type : (DEFAULT) ") 
                self.type = judge.Appropriate(self.type,"DEFAULT").checkType()
                
                if self.type.upper().strip() == "COPY": # to backup file and directory
                    fs.FileSystem().buildDirectory()
                elif self.type.upper().strip() == "DELETE": # delete backup file
                    fs.FileSystem().deleteDirectory()
                    continue
                
                self.size = input("> Enter Size : (100x100) ")
                self.size = judge.Appropriate(self.size,"100,100").checkType()
                self.size = self.size.replace("(","").replace(")","")
                self.size = tuple(map(int,re.split(",|x|X| ",self.size.strip())))
                    
                # do image deal with 
                feature.Switch().tryTest(self.doPath,self.size,self.type)
                Msg.Message.msgMessage(3,"path: {:10} , type: {:10} , size: {:10}".format(self.doPath,self.type,str(self.size)))

        # except:
        #     print("\nfinally")
            