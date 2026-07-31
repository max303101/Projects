import React, { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';
import Row from 'react-bootstrap/Row';
import ListGroup from 'react-bootstrap/ListGroup';

export function Home()
{
    const [cars, setCars] = useState([]);
    const [loaded, setLoaded] = useState(false)

    useEffect(() => 
    {
        fetch('http://localhost:8000/all')
        .then(response => response.json())
        .then(data => 
        {
            console.log(data);
            setCars(data);
        })
        .catch(error => console.error('Error:', error))
        setLoaded(true);
    }, [])

    if(loaded)
    {
        return (
            <div className="bg-dark text-white">
                <Container fluid>
                    <Row xs={1} md={2} className="g-4">
                        {cars.map(car => (
                            <Card style={{ width: '18rem', margin: '10px'}} border="info" data-bs-theme='dark'>
                                <Card.Img style={{ height: '200px', marginTop: '10px'}} variant="top" src={car.podglad} alt='car' rounded/>
                                <Card.Body>
                                    <Card.Title>{car.marka}</Card.Title>
                                    <Card.Subtitle>{car.model}</Card.Subtitle>
                                </Card.Body>
                                <ListGroup className="list-group-flush" style={{ marginBottom: '20px' }}>
                                    <ListGroup.Item>Rocznik: {car.rocznik}</ListGroup.Item>
                                    <ListGroup.Item>Kolor: {car.kolor}</ListGroup.Item>
                                    <ListGroup.Item>Stan: {car.stan}</ListGroup.Item>
                                    <ListGroup.Item>Dostępnych: {car.dostep}</ListGroup.Item>
                                    <ListGroup.Item style={{ font: 'caption', fontSize: '110%'}}>{car.cena} zł</ListGroup.Item>
                                </ListGroup>
                            </Card>))}
                    </Row>
                </Container>                
            </div>
        );
    }
}