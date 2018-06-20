FROM grpc/python:1.4
ADD eligibility_server.py .
ADD eligibility.py .
ADD eligibility_pb2.py .
ADD eligibility_pb2_grpc.py .
EXPOSE 50051
CMD ["python","-u","./eligibility_server.py"]
