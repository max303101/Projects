document.getElementById('submit').addEventListener("click", czyPalindrom);

function wykonaj(e)
{
    e.preventDefault();
    let slowo = document.getElementById('slowo').value;
    console.log(slowo);
    return;
}


function czyPalindrom(e)
{
    e.preventDefault();
    const slowo = document.getElementById('slowo').value;
    const slowo_split = slowo.split("");
    const slowo_split_str = slowo_split.toString();
    const slowo_rev = slowo_split.reverse();
    const slowo_rev_str = slowo_rev.toString();
    if(slowo_split_str == slowo_rev_str)
    {
        console.log(slowo, " to palindrom");
    }
    else
    {
        console.log(slowo, " to nie palindrom");
    }
}
