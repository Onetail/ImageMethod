from PIL import Image
import os 
import assets.feature.filesystem as fs
import assets.message.MessageManage as Msg

class Switch:
	imageaddress = [""]
	imagetype = ["default","copy","normal"]
	def __init__(self,ftype="JPEG"):
		self.ftype = ftype 
		self.image = None
		self.fname = None

	def imageChangesize(self,fsize,fname):
		img = Image.open(fname)
		self.fname = fname
		self.image = img.resize(fsize,Image.ANTIALIAS) #resize image with high-quality
		return self

	def imageSavetype(self):
		self.image.save(self.fname,self.ftype)
		return self

	def imageCopy(self,fname,savelocate):
		self.fname = os.getcwd()+savelocate+fname
		return self

	
	def tryTest(self,locate,fsize,type,savelocate=""):
		if self.modelCheck(locate,type) == "tt":
			for addr,dire,fi in os.walk(locate):
				for i in range(len(fi)):
					if fi[i].endswith(".jpg") or fi[i].endswith(".jpeg") or fi[i].endswith(".png"):
						self.imageChangesize(fsize,addr+fi[i])
						self.imageCopy(fi[i],"/"+savelocate)
						if type.upper().strip()=="COPY":
							self.imageCopy(fi[i],"/Backup/"+savelocate)
						self.imageSavetype()
			Msg.Message.sucMessage(2," Finished work!")

		elif self.modelCheck(locate,type) == "ft":
			Msg.Message.errMessage(3)


	def modelCheck(self,locate,type):
		check = [False,False]
		# check image type
		for i in self.imagetype:
			if type.upper().strip() == i.upper():
				check[0] = True			
		# check address 
		# pass
		# return 
		if check[0] == True:
			return "tt"
		elif check[0] == False:
			return "ft"