import grpc

import employee_service_pb2
import employee_service_pb2_grpc

empDB=[
 {
 'id':101,
 'name':'Saravanan S',
 'title':'Technical Leader'
 },
 {
 'id':201,
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 }
 ]

class EmployeeServer(employee_service_pb2_grpc.EmployeeServicer):

  def CreateEmployee(self, request, context):
    dat = {
    'id':request.id,
    'name':request.name,
    'title':request.title
    }
    empDB.append(dat)
    return employee_service_pb2.StatusReply(status='OK')

  def GetEmployeeDataFromID(self, request, context):
    usr = [ emp for emp in empDB if (emp['id'] == request.id) ] 
    return employee_service_pb2.EmployeeData
