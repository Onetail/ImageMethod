from PIL import Image
import assets.feature.filesystem as fs

class Switch:
	def __init__(self,fname="",ftype="JPEG"):
		self.ftype = ftype 
		self.fname = fname
		self.image = None

	def imageSize(self,fsize):
		img = Image.open(self.fname)
		self.image = img.resize(fsize,Image.ANTIALIAS) #resize image with high-quality
		return self

	def imageSavetype(self):
		# self.image.save(self.fname+"_",self.ftype)
		return self

	def imageCopy(self):
		pass 

	def tryTest(self,locate):
		pass

	def userLocate(self):
		return fs.FileSystem().getUserlocate()		
