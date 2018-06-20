
# coding: utf-8

# In[ ]:


import grpc
from concurrent import futures
import concurrent.futures
#import aiotasks
import time
import eligibility_pb2
import eligibility_pb2_grpc
import eligibility as ea
_ONE_DAY_IN_SECONDS = 60*60*24
class VotingEligibility():
    def getDetails(self, request, context):
    #print('Server side -- Data in request ',request)   
        print('name')
        print('Nationality')
        print("adhaar_id")
        
        return eligibility_pb2.Status(status = "Valid")
    def getAge(self, request, context):
        res = ea.get_age(request.age)
        return eligibility_pb2.Eligibility( eligible = res)
    
def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    eligibility_pb2_grpc.add_VotingEligibilityServicer_to_server( VotingEligibility(),server)
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('localhost:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except keyboardInterrupt:
        server.stop()
        
if __name__ == '__main__':
    server()
        
                                           

