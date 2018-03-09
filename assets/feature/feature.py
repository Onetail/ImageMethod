from PIL import Image
import os 
import assets.feature.filesystem as fs


class Switch:
	def __init__(self,ftype="JPEG"):
		self.ftype = ftype 
		self.image = None
		self.fname = None

	def imageSize(self,fsize,fname):
		img = Image.open(fname)
		self.fname = fname
		self.image = img.resize(fsize,Image.ANTIALIAS) #resize image with high-quality
		return self

	def imageSavetype(self):
		self.image.save(self.fname,self.ftype)
		return self

	def imageCopy(self,fname):
		self.fname = os.getcwd()+"/Backup/"+fname
		return self

	def tryTest(self,locate,fsize,type):
		for addr,dire,fi in os.walk(locate):
			for i in range(len(fi)):
				self.imageSize(fsize,addr+fi[i])
				if type.upper().strip()=="COPY":
					self.imageCopy(fi[i])
				self.imageSavetype()
		# self.imageSize(locate,fsize)
