const express = require('express')
const app = express()
const cors = require('cors')
const mysql = require('mysql')
const multer = require('multer')
const path = require('path')
const fs = require('fs')

app.use(express())
app.use(cors())

const upload = multer({
    dest: 'uploads/',
    limits: { fileSize: 10000000}
})

const pool = mysql.createPool(
    {
        host: 'localhost',
        user: 'root',
        password: '',
        database: 'komis2'
    }
)

app.get('/all', (req, res) => {
    pool.query('SELECT id, marka, model, rocznik, kolor, stan, dostep, cena, podglad FROM samochody', (err, result) => {
        if (err) return res.status(500).json({ error: err.message });
        result.forEach(car => {
            if (car.podglad) {
                const filePath = path.join(__dirname, 'uploads', `${car.id}.png`);
                fs.writeFileSync(filePath, car.podglad, 'binary');
                car.podglad = `http://localhost:8000/uploads/${car.id}.png`;
            }
        })
        res.json(result);
    })
})

app.get('/uploads/:filename', (req, res) =>
{
    res.sendFile(path.join(__dirname, 'uploads', req.params.filename))
})


app.get('/car/:id', (req, res) =>
{
    pool.query(`SELECT id, marka, model, rocznik, kolor, stan, dostep, cena, podglad FROM samochody WHERE id = ${req.params.id}`, (err, result) =>
    {
        if(err) throw err

        if(result[0].podglad)
        {
            const filePath = path.join(__dirname, 'uploads', `${result[0].id}.png`)

            fs.writeFile(filePath, result[0].podglad, 'binary', (err) =>
            {
                result[0].podglad = `http://localhost:8000/uploads/${result[0].id}.png`
                res.json(result)
            })
        }
        else
        {
            res.json(result)
        }
    })
})

app.get('/zamow/:samochody_id/:imie/:nazwisko/:telefon', (req, res) => 
    {
        if(req.params.samochody_id == 0 || req.params.samochody_id == null)
        {
            res.json("Proszę wybrać samochód...")
            return 0;
        }
        pool.query(`SELECT dostep FROM samochody WHERE id=${req.params.samochody_id}`, (err, result) =>
        {
            if(err) throw err
            if(result[0].dostep == 0)
                {
                    res.json("Niestety, wybrany samochód jest już zamówiony...")
                }
                else
                {
                    pool.query(`INSERT INTO zamowienia (id, samochody_id, klient, telefon, dataZam) VALUES (NULL, ${req.params.samochody_id}, '${(req.params.imie + " " + req.params.nazwisko)}', ${req.params.telefon}, CURRENT_TIMESTAMP)`, (err, result) =>
                    {
                        if (err) throw err
                    })
                    pool.query(`UPDATE samochody SET dostep = dostep - 1 WHERE id=${req.params.samochody_id}`, (err, result) =>
                    {
                        if (err) throw err
                    })
                    res.json("Zamówienie zostało złożone...")
                }
        })
    })

app.get('/zamowienia/all', (req, res) => 
{
    pool.query(`SELECT zamowienia.klient, zamowienia.telefon, samochody.marka, samochody.model, samochody.rocznik, samochody.kolor, samochody.stan, samochody.cena, DATE_FORMAT(zamowienia.dataZam, '%Y-%m-%d') as dataZam FROM samochody, zamowienia WHERE samochody.id = zamowienia.samochody_id`, (err, result) =>
    {
        if (err) return res.status(500).json({ error: err.message });
        res.json(result);
    })
})

console.log('Serwer nasłuchuje na porcie 8000')
app.listen(8000)