import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
import time
import sys

if len(sys.argv) != 3:
	print "Input the argument including the projectId and board masterId"
	exit(-1)

projectId = sys.argv[1]
masterId = sys.argv[2]
sensorAId = "Jarvis"
sensorBId = "Friday"
# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': projectId,
})

db = firestore.client()
docBoard_ref = db.collection(u'board').document(masterId)
docSensorA_ref = db.collection(u'sensor').document(sensorAId)
docSensorB_ref = db.collection(u'sensor').document(sensorBId)
samplingARate = random.randint(10,30)
samplingBRate = random.randint(10,30)
while True:
	cpuTemperature = random.uniform(40, 60)
	diskUsage = random.uniform(30, 60)
	gpuTemperature = random.uniform(50, 80)
	memoryUsage = random.uniform(30, 60)
	docBoard_ref.set({
		u'cpuImage': u'pi',
		u'cpuTemperature': cpuTemperature,
		u'diskUsage': diskUsage,
		u'geoInfo': u'San Diegos',
		u'gpuTemperature': gpuTemperature,
		u'memoryUsage': memoryUsage})

	errorRate = random.uniform(0, 1)
	sampledValue = random.uniform(20,30)
	docSensorA_ref.set({
		u'errorRate': errorRate,
		u'masterId': unicode(masterId),
		u'model':unicode(sensorAId),
		u'sampledValue': sampledValue,
		u'samplingRate': samplingARate
		})

	errorRate = random.uniform(0, 1)
	sampledValue = random.uniform(20,30)
	docSensorB_ref.set({
		u'errorRate': errorRate,
		u'masterId': unicode(masterId),
		u'model':unicode(sensorBId),
		u'sampledValue': sampledValue,
		u'samplingRate': samplingBRate
		})
	print "Update sensor info successfully"
	time.sleep(5)
