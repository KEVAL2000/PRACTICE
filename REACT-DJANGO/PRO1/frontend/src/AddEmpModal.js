import React, {Component} from 'react';
import {Modal, Button, Row, Col, Form, Image} from 'react-bootstrap';

export class AddEmpModal extends Component {
    constructor(props) {
        super(props);
        this.state = {deps: []};
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleFileSelected = this.handleFileSelected.bind(this);
    }

    photofilename = 'anonymous.png';
    imagesrc = process.env.REACT_APP_PHOTOPATH + this.photofilename;

    componentDidMount() {
        fetch(process.env.REACT_APP_API + 'department')
        .then(response => response.json())
        .then(data => {
            this.setState({deps: data});
        });
    }

    handleSubmit(event) {
        event.preventDefault();
        fetch(process.env.REACT_APP_API + 'employee', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body:JSON.stringify({
                EmployeeId: null,
                EmployeeName: event.target.EmployeeName.value,
                Department: event.target.Department.value,
                DateOfJoining: event.target.DateOfJoining.value,
                PhotoFileName: this.photofilename
            })
        })
        .then(res => res.json())
        .then((result) => {
            alert(result);
        }, (error) => {
            alert('Failed');
        })
    }

    handleFileSelected(event) {
        event.preventDefault();
        this.photofilename = event.target.files[0].name;
        const formData = new FormData();
        formData.append(
            'myFile',
            event.target.files[0],
            event.target.files[0].name
        );

        fetch(process.env.REACT_APP_API + 'employee/saveFile', {
            method: 'POST',
            body: formData
        })
        .then(res => res.json())
        .then((result) => {
            this.imagesrc = process.env.REACT_APP_PHOTOPATH + result;
        }, (error) => {
            alert('Failed');
        })
    }

    render() {
        return (
            <div className='container'>
                <Modal {...this.props} size='lg' aria-labelledby='contained-modal-title-vcenter' centered>
                    <Modal.Header closeButton>
                        <Modal.Title id='contained-modal-title-vcenter'>
                            Add Employee
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <Row>
                            <Col sm={6}>
                                <Form onSubmit={this.handleSubmit}>
                                    <Form.Group controlId='EmployeeName'>
                                        <Form.Label>Employee Name</Form.Label>
                                        <Form.Control type='text' name='EmployeeName' required placeholder='Employee Name' />
                                    </Form.Group>
                                    <Form.Group controlId='Department'>
                                        <Form.Label>Department</Form.Label>
                                        <Form.Control as='select'>
                                            {this.state.deps.map(dep => <option key={dep.DepartmentId}>{dep.DepartmentName}</option>)}
                                        </Form.Control>
                                    </Form.Group>
                                    <Form.Group controlId='DateOfJoining'>
                                        <Form.Label>Date Of Joining</Form.Label>
                                        <Form.Control type='date' name='DateOfJoining' required placeholder='Date Of Joining' />
                                    </Form.Group>
                                    <Form.Group>
                                        <Button varient='primary' type='submit'>
                                            Add Employee
                                        </Button>
                                    </Form.Group>
                                </Form>
                            </Col>

                            <Col sm={6}>
                                <Image width='200px' height='200px' src={this.imagesrc} />
                                <input type='File' onChange={this.handleFileSelected} />
                            </Col>
                        </Row>
                    </Modal.Body>

                    <Modal.Footer>
                        <Button varient='danger' onClick={this.props.onHide}>Close</Button>
                    </Modal.Footer>
                </Modal>
            </div>
        )
    }
}