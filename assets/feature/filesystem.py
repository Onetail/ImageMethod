import os 
import assets.message.MessageManage as Msg
import assets.module.judge as judge 


class FileSystem:
    def __init__(self):
        self.username = self.getUsername()
        self.userlocate = os.getcwd()+"/assets/image/"

    def buildDirectory(self,backup="Backup"):
        if not os.path.exists(os.getcwd()+"/"+backup):
            os.mkdir(backup)
        
    def deleteDirectory(self,backup="Backup"):
        if os.path.exists(os.getcwd()+"/"+backup):
            # 判斷
            check = input("Are you sure delete directory ? (yes) ")
            check = judge.Appropriate(check,"yes").checkType()
            if check.upper().strip() == "YES":
                # 若肯定
                os.rmdir(os.getcwd()+"/"+backup)
                Msg.Message.sucMessage(2,"已刪除 "+os.getcwd()+"/"+backup)
                pass 
            else :
                # 若不肯定
                Msg.Message.msgMessage(2,"")
                return 
        else:
            Msg.Message.errMessage(2)

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