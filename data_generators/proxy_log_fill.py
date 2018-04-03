import random
import time

sleep_time=2  #seconds
rec_count=50000
for x in range(rec_count):
	ycnt = random.randint(1, 20)
	for y in range(ycnt):
		print('{"time_taken":' + str(random.randint(2, 50))+ ', "timestamp" : '+ str(time.time()).split(".")[0] +', "cs_byte" : '+str(random.randint(1500, 40000))+',"sc_byte" : '+ str(random.randint(1500, 40000))+',"cs_host" : "'+random.choice (['github.com','badsite.com','reallybadsite.com','harmful.com','malicious.com','notthisone.com'])+'", "categories" : '+ str(random.sample(["badsite","malicious_site","harmful_site","blocked_site","unapproved_site","non_work_related_site"],3)).replace('\'','"') + ',"pg" : "'+random.choice (["pg1","pg2","pg3","pg4","pg5"]) +'" }')
	time.sleep(sleep_time)

