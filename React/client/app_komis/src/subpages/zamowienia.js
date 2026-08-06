import '../App.css';
import Table from 'react-bootstrap/Table'
import Container from 'react-bootstrap/Container';

import React, { useState, useEffect } from 'react';

export function Zamowienia()
{
    const [zamowienia, setZamowienia] = useState([])
    
    useEffect(() => 
    {
        fetch('http://localhost:8000/zamowienia/all')
        .then(response => response.json())
        .then(data => setZamowienia(data))
        .catch(error => console.error('Error:', error))
    }, [])

    return(
        <div className="bg-dark text-white" style={{ height: '100%' }}>
            <Container className="bg-dark text-white" style={{ textAlign: 'center' }} fluid>
                <h2>Zamówienia</h2>
                <Table striped hover variant="dark">
                <thead>
                    <tr>
                        <th>Imię i nazwisko</th>
                        <th>Nr telefonu</th>
                        <th>Samochód</th>
                        <th>Data zamówienia</th>
                    </tr>
                </thead>
                <tbody>
                    {zamowienia.map(zamowienie => 
                    (
                        <tr>
                            <td>{zamowienie.klient}</td>
                            <td>{zamowienie.telefon}</td>
                            <td>{zamowienie.marka} {zamowienie.model} | {zamowienie.rocznik} | {zamowienie.kolor} | {zamowienie.stan} | {zamowienie.cena}zł</td>
                            <td>{zamowienie.dataZam}</td>
                        </tr>
                    ))}
                </tbody>
                </Table>
                
            </Container>
        </div>
    )

    
}