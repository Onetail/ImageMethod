import os 
import assets.message.MessageManage as Msg

class FileSystem:
    def __init__(self):
        self.username = self.getUsername()
        self.userlocate = "/Users/"+self.username

    def buildDirectory(self):
        pass
    
    def deleteDirectory(self):
        pass 

    def moveDirectory(self):
        pass 

    def lookDirectory(self,path="/Users/chuyuwei/Desktop/"):
        for addr,dire,fi in os.walk(path):
            for j in range(len(fi)):
                Msg.Message.msgMessage(number=2,txt=addr+"/"+fi[j])

        self.getUsername()
        return self

    def getUsername(self):
        return os.getlogin()

    def getUserlocate(self):
        return self.userlocate