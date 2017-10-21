import urllib.request
import re
''' TODO: 
		save status of cars
		save images of cars and hash function
		multi-thread()'''
		
# car class
class Car(object):
	Status = None
	Number = None
	Name = None
	VIN = None
	ExColor = None
	InColor = None
	Engine = None
	Transmission = None
	Drivetrain = None
	MPG = None
	FuelType = None
	
	price = 0
	
	def print(self):
		print(self.Name)
		print(self.Number)
		print(self.VIN)
		print(self.ExColor)
		print(self.InColor)
		print(self.Engine)
		print(self.Transmission)
		print(self.Drivetrain)
		print(self.MPG)
		print(self.FuelType)
		print(self.Status)


def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	return html

def getImg(html, number):
	reg = r'&quot;https://www.cstatic-images.com/results(.+?\.jpg)&quot;'
	imgre = re.compile(reg)
	imgList = re.findall(imgre, html)
	x = 0
	for img in imgList:
		imgURL =  "https://www.cstatic-images.com/supersized" + img
		imgName = str(number) + "-" + str(x) + ".jpg"
		urllib.request.urlretrieve(imgURL, imgName)	
		#print(imgURL)
		x = x + 1
	#imgPage = urllib.request.urlopen("https://images.autotrader.com/scaler/653/490/hn/c/aa520fb160d44d3b8872b85912ac6cd2.jpg")
	#urllib.request.urlretrieve("https://images.autotrader.com/scaler/653/490/hn/c/aa520fb160d44d3b8872b85912ac6cd2.jpg",'test.jpg')	

def getInfo(html,number):
	html = html.decode('utf-8')#python3
	tempCar = Car()

	tempCar.Number = number
	
	getImg(html, number)

	#get the price of the car
	pattern = re.compile(r'<div class="vdp-cap-price__price">\$(.*)</div>')
	priceList = re.findall(pattern, html);
	tempCar.price = priceList[0]
	
	#get the name of the car
	pattern = re.compile(r'<h1 class="vdp-cap-mmy__heading">(.*)</h1>')
	nameList = re.findall(pattern, html);	
	tempCar.Name = nameList[0]
	
	#get the exterior color
	pattern = re.compile(r'Exterior Color:</strong>\n\s+(.*)\n')
	exColorList = re.findall(pattern, html);
	if exColorList != []:
		tempCar.ExColor = exColorList[0]

	#get the interior color
	pattern = re.compile(r'Interior Color:</strong>\n\s+(.*)\n')
	inColorList = re.findall(pattern, html);	
	if inColorList != []:
		tempCar.InColor = inColorList[0]

	#get the VIN of the car
	pattern = re.compile(r'VIN:</strong>\n\s+(.*)\n')
	VINList = re.findall(pattern, html);	
	if VINList != []:
		tempCar.VIN = VINList[0]

	#get the engine of the car
	pattern = re.compile(r'Engine:</strong>\n\s+(.*)\n')
	engineList = re.findall(pattern, html);	
	if engineList != []:
		tempCar.Engine = engineList[0]
		
	pattern = re.compile(r'Transmission:</strong>\n\s+(.*)\n')
	TransmissionList = re.findall(pattern, html);	
	if TransmissionList != []:
		tempCar.Transmission = TransmissionList[0]
		
	pattern = re.compile(r'Drivetrain:</strong>\n\s+(.*)\n')
	DrivetrainList = re.findall(pattern, html);	
	if DrivetrainList != []:
		tempCar.Drivetrain = DrivetrainList[0]
	
	pattern = re.compile(r'MPG:</strong>\n\s+(.*)\n')
	MPGList = re.findall(pattern, html);	
	if MPGList != []:
		tempCar.MPG = MPGList[0]
		
	pattern = re.compile(r'FuelType:</strong>\n\s+(.*)\n')
	FuelTypeList = re.findall(pattern, html);	
	if FuelTypeList != []:
		tempCar.FuelType = FuelTypeList[0]

	tempCar.Status = tempCar.Name.split(' ')[0]	
	tempCar.print()

# get all number of cars
def getCarsList(html):
	pattern = re.compile(r'data-goto-vdp="(.*)"')
	html = html.decode('utf-8')#python3
	carsList = re.findall(pattern, html)
	carsList = list(set(carsList))
	return carsList

print ("testing")
#getImg()
html = getHtml("https://www.cars.com/vehicledetail/detail/716436878/overview/")
#getInfo(html)
# only for test use
carsList = getCarsList(getHtml("https://www.cars.com/shopping/lexus/?page=1&perPage=25"))
for carNumber in carsList:
	carUrl = "https://www.cars.com/vehicledetail/detail/" + carNumber + "/overview/"
	getInfo(getHtml(carUrl),carNumber)
	print("\n")