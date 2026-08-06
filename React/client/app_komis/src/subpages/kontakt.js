import Container from 'react-bootstrap/Container';
import '../App.css';

export function Kontakt ()
{
    return (
        <div className="bg-dark text-white" style={{ height: '100%' }}>
            <Container className="bg-dark text-white" style={{ textAlign: 'center' }} fluid>
                <h2>Kontakt</h2>
                <p>Maksymilian Borys</p>
            </Container>
        </div>
    )
}