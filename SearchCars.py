import urllib
import urllib2
import re
import webbrowser

class SearchCars(object): 

	urlO = "https://www.cars.com/for-sale/searchresults.action/?"
	item = ['mkId=', '&mdId=', '&prMx=', '&rd=', '&zc=', '&stkTypId=', '&cpoId=',
		'&searchSource=PAGINATION', '&sort=relevance', '&perPage=100', '&page=1',
		'&page=']
	makeD = {}
	statusD = {}
	modelD = {}

	def __init__(self):
		self.getInfo()

	def getInfo(self):
		makeF = open('make.txt', 'r') 
		makeC = makeF.read()
		makeP = re.compile(r'<option value="\d*">.*</option>')
		makeL = re.findall(makeP, makeC)

		for i in makeL: 
			tempP = re.compile(r'\d+')
			tempP2 = re.compile(r'>.*<')
			num = re.findall(tempP, i)
			name = re.findall(tempP2, i)
			name[0] = name[0].strip('<')
			name[0] = name[0].strip('>')
			self.makeD[name[0]] = num[0]

		statusF = open('status.txt', 'r')
		statusC = statusF.read()
		statusP = re.compile(r'\n')
		statusP2 = re.compile(r' = ')
		statusL = statusP.split(statusC)
		for i in statusL:
			tempL = statusP2.split(i)
			self.statusD[tempL[0]] = tempL[1]

		modelF = open('model.txt', 'r')
		modelC = modelF.read()
		modelP = re.compile(r'</select>', re.S)
		modelL = modelP.split(modelC)

		for i in modelL: 
			tempP = re.compile(r'<option.*?</option>')
			tempL = re.findall(tempP, i)
			for j in tempL: 
				if ',' in j: 
					continue
				tempP2 = re.compile(r'\d+')
				tempP3 = re.compile(r'>.*<')
				num = re.findall(tempP2, j)
				name = re.findall(tempP3, j)
				name[0] = name[0].strip('<')
				name[0] = name[0].strip('>')
				name[0] = name[0].strip(' - ')
				self.modelD[name[0]] = num[0]

	def search(self, make, typeId, moId, priceMax, radius, zipCode): 

		makeId = ''
		typId = ''
		modelId = ''
		pMax = ''
		rd = ''
		zc = ''

		if (make != ''): 
			makeId = self.makeD[make]
		if (typeId != ''):
			typId = self.statusD[typeId]
		if (moId != ''):
			modelId = self.modelD[moId]
		if (priceMax != ''):  
			pMax = priceMax
		if (radius != ''):
			rd = radius
		if (zc != ''):
			zc = zipCode

		'''
		makeId = '20005'
		typId = ''
		modelId = '21392'
		pMax = '175000'
		rd = '99999'
		zc = '92122'
		'''

		url = self.urlO
		url += self.item[0]
		url += makeId
		url += self.item[1]
		url += modelId
		url += self.item[2]
		url += pMax
		url += self.item[3]
		url += rd
		url += self.item[4]
		url += zc
		url += self.item[5]
		if (typId != '28444'):  
			url += typId
		url += self.item[6]
		if (typId == '28444'): 
			url += typId
		url += self.item[7]
		url += self.item[8]
		url += self.item[9]
		url += self.item[10]
		webbrowser.open(url)


		page = 0
		finalList = []
		try: 
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			content = response.read()
			pattern = re.compile(r'<div id="listing-.*?"'
				' class="shop-srp-listings__listing"')
			pattern2 = re.compile(r'searchresults.action.*?Page=')
			plist = re.findall(pattern, content)
			plist2 = re.findall(pattern2, content)
			pattern3 = re.compile(r'\d+')
			plist3 = re.findall(pattern3, plist2[len(plist2) - 1])
			page = int(plist3[0])
			url2 = 'https://www.cars.com/vehicledetail/detail/'
			for i in plist: 
				tempP = re.compile(r'\d+')
				tempL = re.findall(tempP, i)
				tempURL = url2 + tempL[0] + '/overview/'
				finalList.append(tempURL)
			
		except urllib2.URLError, e: 
			if hasattr(e, 'code'): 
				print e.code
			if hasattr(e, 'reason'): 
				print e.reason

		for i in range(1, page+1): 
			url = self.urlO
			url += self.item[0]
			url += makeId
			url += self.item[1]
			url += modelId
			url += self.item[2]
			url += pMax
			url += self.item[3]
			url += rd
			url += self.item[4]
			url += zc
			url += self.item[5]
			if (typId != '28444'):  
				url += typId
			url += self.item[6]
			if (typId == '28444'): 
				url += typId
			url += self.item[7]
			url += self.item[8]
			url += self.item[9]
			url += self.item[11]
			url += str(i)
			#webbrowser.open(url)


			try: 
				request = urllib2.Request(url)
				response = urllib2.urlopen(request)
				content = response.read()
				pattern = re.compile(r'<div id="listing-.*?"'
					' class="shop-srp-listings__listing"')
				url2 = 'https://www.cars.com/vehicledetail/detail/'
				for i in plist: 
					tempP = re.compile(r'\d+')
					tempL = re.findall(tempP, i)
					tempURL = url2 + tempL[0] + '/overview/'
					finalList.append(tempURL)
				
			except urllib2.URLError, e: 
				if hasattr(e, 'code'): 
					print e.code
				if hasattr(e, 'reason'):
					print e.reason
		return finalList
