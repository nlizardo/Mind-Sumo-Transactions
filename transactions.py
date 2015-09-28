#MindSumo Challenge
import datetime

def calculateDuration(startDate, endDate):
		x = startDate.split('/')
		y = endDate.split('/')
		start = datetime.date(int(x[2]), int(x[0]), int(x[1]))
		end = datetime.date(int(y[2]), int(y[0]), int(y[1]))

		dur = end - start
		return dur
class Subscription():
	def __init__(self, subscriptionId, startDate):
		self.id = subscriptionId
		self.subscriptionType = 'one-off'
		self.startDate = startDate
		self.endDate = ''
	def getType(self, endDate):

		dur = calculateDuration(self.startDate, endDate)
		Monthly = datetime.timedelta(28)
		yearly = datetime.timedelta(365)
		#print dur
		if dur >= yearly:
			self.subscriptionType = 'Yearly'
		elif dur >= Monthly:
			self.subscriptionType = 'Monthly'
		else:
			self.subscriptionType = 'Daily'

	def __str__(self):
		return "Subscription ID: %s \nSubscription Type: %s " % (self.id, self.subscriptionType)
		#return "HI"
f = open('subscription_report.csv', 'r')
subscriptionDict = {}
yearDict={}
count = 0
for line in f:
	x = line.split(',')
	if x[0] == "Id":
		continue
	date = x[3].split('/')
	year = int(date[-1])
	if year not in yearDict.keys():
		yearDict[year] = int(x[2])
	else:
		yearDict[year] += int(x[2])
	print "Parsing id: %s" % (x[0])
	#if count == 100000:
	#	break
	if x[1] not in subscriptionDict.keys():
		s = Subscription(x[1], x[3])
		subscriptionDict[x[1]] = s
	else:
		if subscriptionDict[x[1]].subscriptionType == 'one-off':
			subscriptionDict[x[1]].getType(x[3])
			subscriptionDict[x[1]].endDate = x[3]
		else:
			subscriptionDict[x[1]].endDate = x[3]

#Output challenge question
for a in subscriptionDict.keys():
	print subscriptionDict[a]
	if subscriptionDict[a].subscriptionType == "one-off":
		print "Duration: one-off"
	else:
		dur = calculateDuration(subscriptionDict[a].startDate, subscriptionDict[a].endDate)
		print "Duration: " + str(dur)

#Bonus challenge 1
print "\n\nBONUS QUESTION 1 \n\n"

revenueGrowthDict = {}
print "Revenue per year"
for year in yearDict.keys():
	print "%s: %d" % (year, yearDict[year])
	if year == 1966:
		continue
	#Subtract then calculate percent then put in dictinoary
	revenue = (float(yearDict[year] - yearDict[year-1])/yearDict[year-1])* 100
	revenueGrowthDict[year] = revenue

yearlyRevenueList = sorted(revenueGrowthDict.keys(), key= lambda k: revenueGrowthDict[k], reverse=True)
print "Years with highest revenue growth:"
print "%d : %d%" % (yearlyRevenueList[0], revenueGrowthDict[yearlyRevenueList[0]])
print "%d : %d%" % (yearlyRevenueList[1], revenueGrowthDict[yearlyRevenueList[1]])
print "%d : %d%" % (yearlyRevenueList[2], revenueGrowthDict[yearlyRevenueList[2]])
print "%d : %d%" % (yearlyRevenueList[3], revenueGrowthDict[yearlyRevenueList[3]])
print "%d : %d%" % (yearlyRevenueList[4], revenueGrowthDict[yearlyRevenueList[4]])

print "Years with lowest revenue growth"
print "%d : %d%" % (yearlyRevenueList[-1], revenueGrowthDict[yearlyRevenueList[-1]])
print "%d : %d%" % (yearlyRevenueList[-2], revenueGrowthDict[yearlyRevenueList[-2]])
print "%d : %d%" % (yearlyRevenueList[-3], revenueGrowthDict[yearlyRevenueList[-3]])
print "%d : %d%" % (yearlyRevenueList[-4], revenueGrowthDict[yearlyRevenueList[-4]])
print "%d : %d%" % (yearlyRevenueList[-5], revenueGrowthDict[yearlyRevenueList[-5]])

f.close()