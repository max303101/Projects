import '../App.css';
import { useEffect, useState } from "react";
import Container from 'react-bootstrap/Container';
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
// import Prompt from 'react-router/Prompt';


export function Zamow()
{
    const [cars, setCars] = useState([])
    
    
    useEffect(() => 
        {
            fetch('http://localhost:8000/all')
           .then(response => response.json())
           .then(data => setCars(data))
           .catch(error => console.error('Error:', error))
        }, [])

    const onSumbit = (e) => 
        {
            e.preventDefault();
            const imie = document.getElementById("imie").value
            const nazwisko = document.getElementById("nazwisko").value
            const wybor = document.getElementById("wybor").value
            const telefon = document.getElementById("telefon").value


            
            fetch(`http://localhost:8000/zamow/${wybor}/${imie}/${nazwisko}/${telefon}`)
            .then(response => response.json())                    //ZROBIĆ TAK ŻEBY WYŚWITLAŁY SIĘ ODPOWIEDZI Z SERWERA PS TO NIE DZILA
            .then(data => alert(data))
            .catch(error => console.error('Error: ', error))


            
            
        }



    return (
        <div className="zamowienie bg-dark text-white" style={{ height: '100%' }}>
        
            <Container fluid>
                <h1>Zamówienie</h1>
                <Form onSubmit={onSumbit} data-bs-theme='dark'>
                    <Row className="mb-3">
                        <Form.Group as={Col} controlId="formGridImie">
                            <FloatingLabel label="Imię...">
                                <Form.Control id="imie" type="text" placeholder="Imię..." required/>
                                
                            </FloatingLabel>
                        </Form.Group>

                        <Form.Group as={Col} controlId="formGridNazwisko">
                            <FloatingLabel label="Nazwisko...">
                                <Form.Control id="nazwisko" type="text" placeholder="Nazwisko..." required/>
                            </FloatingLabel>
                        </Form.Group>

                        <Form.Group as={Col} controlId="formGridTelefon">
                            <FloatingLabel label="Telefon...">
                                <Form.Control id="telefon" type="number" placeholder="Telefon..." required/>
                            </FloatingLabel>
                        </Form.Group>
                    </Row>

                    <Form.Group className="mb-3" controlId="formGridSamochod">
                        <FloatingLabel label="Wybierz samochód">
                            <Form.Select id="wybor" >
                                <option value={0}></option>
                                {cars.map(car => 
                                    (
                                        <option value={car.id}>{car.marka} {car.model} | {car.rocznik} | {car.stan}</option>
                                    ))}
                            </Form.Select>
                        </FloatingLabel>
                    </Form.Group>

                    <Button variant="primary" type="submit">Zamów</Button>
                </Form>
            </Container>
        </div>
    )
}