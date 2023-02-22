import React, {Component} from 'react';
import {Table} from 'react-bootstrap';
import {Button, ButtonToolbar} from 'react-bootstrap';
import { AddEmpModal } from './AddEmpModal';
import { EditEmpModal } from './EditEmpModal';

export class Employee extends Component {

    constructor(props) {
        super(props);
        this.state = {emps: [], addModalShow: false, editModalShow: false}
    }

    refreshList() {
        fetch(process.env.REACT_APP_API + 'employee')
        .then(response => response.json())
        .then(data => {
            this.setState({emps: data});
        });
    }

    componentDidMount() {
        this.refreshList();
    }

    componentDidUpdate() {
        this.refreshList();
    }

    deleteEmp(empid) {
        if(window.confirm('Are you sure?')) {
            fetch(process.env.REACT_APP_API + 'employee/' + empid, {
                method: 'DELETE',
                header: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            })
        }
    }

    render() {
        const {emps, empid, empname, dept, photofilename, doj} = this.state;
        let addModalClose = () => this.setState({addModalShow: false});
        let editModalClose = () => this.setState({editModalShow: false});
        console.log(emps);
        return(
            <div>
                <Table className='mt-4' striped bordered hover size='sm'>
                    <thead>
                        <tr>
                            <th>Employee Id</th>
                            <th>Employee Name</th>
                            <th>Department</th>
                            <th>Date Of Joining</th>
                            <th>Options</th>
                        </tr>
                    </thead>
                    <tbody>
                        {emps.map(emp =>
                            <tr key={emp.EmployeeId}>
                                <td>{emp.EmployeeId}</td>
                                <td>{emp.EmployeeName}</td>
                                <td>{emp.Department}</td>
                                <td>{emp.DateOfJoining}</td>
                                <td>
                                    <ButtonToolbar>
                                        <Button className='mr-2' varient='info' onClick={() => this.setState({editModalShow: true, empid: emp.EmployeeId, empname: emp.EmployeeName, dept: emp.Department, doj: emp.DateOfJoining, photofilename: emp.PhotoFileName})}>
                                            Edit
                                        </Button>
                                    </ButtonToolbar>

                                    <EditEmpModal show={this.state.editModalShow} onHide={editModalClose} empid={empid} empname={empname} dept={dept} doj={doj} photofilename={photofilename} />
                                    
                                    <ButtonToolbar>
                                        <Button className='mr-2' varient='danger' onClick={() => this.deleteEmp(emp.EmployeeId)}>
                                            Delete
                                        </Button>
                                    </ButtonToolbar>
                                </td>
                            </tr>
                            )}
                    </tbody>
                </Table>

                <ButtonToolbar>
                    <Button varient='primary' onClick={() => this.setState({addModalShow: true})}>Add Employee</Button>
                    <AddEmpModal show={this.state.addModalShow} onHide={addModalClose} />
                </ButtonToolbar>
            </div>
        )
    }
}