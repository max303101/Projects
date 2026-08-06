document.getElementById('submit').addEventListener("click", czyDoskonala);

function czyDoskonala(e)
{
    e.preventDefault();
    let suma = 0;
    const liczba = document.getElementById('liczba').value;

    for(let i = 1; i <= liczba / 2; i++)
    {
        if(liczba % i == 0)
        {
            suma += i;
        }
    }
    if(suma == liczba)
    {
        console.log("liczba ", liczba, " jest doskonała")
        return;
    }
    else
    {
        console.log("liczba ", liczba, " nie jest doskonała")
    }
}