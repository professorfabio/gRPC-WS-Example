from __future__ import print_function
import logging

import grpc
import employee_service_pb2
import employee_service_pb2_grpc

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = employee_service_pb2_grpc.EmployeeStub(channel)

        # Query an employee's data
        response = stub.GetEmployeeDataFromID(employee_service_pb2.EmployeeID(id=101))
        print ('Employee\'s data: ' + str(response))

        # Add a new employee
        response = stub.CreateEmployee(employee_service_pb2.EmployeeData(id=301, name='Jose da Silva', title='Programmer'))
        print ('Added new employee ' + response.status)

        # Change an employee's title
        response = stub.UpdateEmployeeTitle(employee_service_pb2.EmployeeTitleUpdate(id=301, title='Senior Programmer'))
        print ('Updated employee ' + response.status)

        # Delete an employee
        response = stub.DeleteEmployee(employee_service_pb2.EmployeeID(id=201))
        print ('Deleted employee ' + response.status)

if __name__ == '__main__':
    logging.basicConfig()
    run()