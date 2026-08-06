import { Link } from "react-router-dom";
import Nav from 'react-bootstrap/Nav';

export function Navbar()
{
    return (
        <nav className="bg-dark text-white" style={{ paddingBottom: '30px', paddingLeft: '20px' }}>
            <Nav variant="underline" defaultActiveKey="/">
                <Nav.Item>
                    <Nav.Link><Link to="/" style={{ textDecoration: 'none', color: 'white', fontSize: '130%'}}>Strona główna</Link></Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link><Link to="/zamow" style={{ textDecoration: 'none', color: 'white', fontSize: '130%' }}>Zamów</Link></Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link><Link to="/zamowienia" style={{ textDecoration: 'none', color: 'white', fontSize: '130%' }}>Zamówienia</Link></Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link><Link to="/kontakt" style={{ textDecoration: 'none', color: 'white', fontSize: '130%' }}>Kontakt</Link></Nav.Link>
                </Nav.Item>
            </Nav>
        </nav>
    )
}