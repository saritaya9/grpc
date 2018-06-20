
# coding: utf-8

# In[1]:


import grpc
#import eligibility
import eligibility_pb2
import eligibility_pb2_grpc

def getDetails():
    channel = grpc.insecure_channel('localhost:50051')
    stub = eligibility_pb2_grpc.VotingEligibilityStub(channel)
    
    name = input("enter name")
    nationality = input("enter nationality")
    adhaar_id =  int (input("enter adhaar_id"))
    
    response = stub.getDetails(eligibility_pb2.Details(name = name, nationality = nationality , adhaar_id = adhaar_id))
    print("Client side -- :" , response)
     
    Age =  int (input("enter Age"))
    
     
    response = stub.getAge(eligibility_pb2.Age(age=Age))
    print("Client side -- :" , response )
if __name__ == '__main__':
    getDetails()

    









