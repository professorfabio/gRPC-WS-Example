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
    return employee_service_pb2.EmployeeData(id=usr[0]['id'], name=usr[0]['name'], title=usr[0]['title'])

  def UpdateEmployeeTitle(self, request, context):
    usr = [ emp for emp in empDB if (emp['id'] == request.id) ]
    usr[0]['title'] = request.title
    return employee_service_pb2.StatusReply(status='OK')

  def DeleteEmployee(self, request, context):
    usr = [ emp for emp in empDB if (emp['id'] == request.id) ]
    if len(usr) == 0:
      return employee_service_pb2.StatusReply(status='NOK')

    empDB.remove(usr[0])
    return employee_service_pb2.StatusReply(status='OK')

  
