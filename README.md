# Reseptisovellus
Sovellus on toteutettu kurssilla Tietokantasovellus (kevät 2022)


https://tsoha-reseptisovellus.herokuapp.com

Sovellusta on mahdollista testata herokussa. Jotta kaikkia toiminnallisuuksia voi kokeilla, tulee sinne ensin luoda oma käyttäjä tai käyttää valmiiksi luotua käyttäjää (käyttäjänimi: testi_käyttäjä, salasana: salasana123). Sivustolla on valmiina ylläpitäjä (käyttäjänimi: admin, salasana: password), mutta ylläpitäjän voi myös luoda itse osoitteessa https://tsoha-reseptisovellus.herokuapp.com/register_admin.

## Sovelluksen kuvaus
Reseptisovelluksella käyttäjä voi hakea tietokantaan lisättyjä reseptejä. Jos käyttäjä haluaa lisätä tietokantaan itse reseptin, hänen tulee ensin rekisteröityä sovellukseen käyttäjätunnuksella ja salasanalla. Tämän jälkeen hän voi kirjautua kyseisellä tunnuksella sovellukseen, ja lisätä reseptejä. Sivustolla on lisäksi olemassa ylläpitäjä, joka pystyy piilottamaan reseptejä.
### Ominaisuudet:
Kuka tahansa pystyy...
- [x] rekisteröidä uuden käyttäjän
- [x] kirjautua sisään jo olemassa olevalla käyttäjällä
- hakea reseptejä...
  - [x] reseptin nimen perusteella
  - [x] reseptin lisääjän käyttäjänimen perusteella
- lajitella näytettävät reseptit...
  - [x] aakkosjärjestyksen mukaan
  - [x] suosion mukaan
  - [x] lisäysajan mukaan
  - [x] reseptin valmistusajan mukaan
  - [x] ruokalajin perusteella
- nähdä, kuinka monta tykkäystä reseptillä on
  
Kirjautunut käyttäjä pystyy...
- [x] lisätä uuden reseptin
- [x] kirjautua ulos käyttäjältä
- [x] kommentoimaan reseptejä
- [x] arvostelemaan reseptejä asteikolla 1-5
- [x] lisätä reseptejä omiin suosikkeihin
- [x] tykätä reseptistä

Ylläpitäjä pystyy...
- [x] piilottamaan reseptin sivustolta ja palauttamaan piilotetun reseptin
- [x] näkemään sivustolle rekisteröityneiden käyttäjien käyttänimet

## Mahdolliset parannuskohdat
Ylläpitäjän rooli jäi hieman turhaksi, sillä vaikka se piilottaisi reseptin, niin sen pystyy silti näkemään osoiterivin kautta, jos tietää reseptin id-numeron. Lisäksi kun käyttäjä on arvostellut reseptin, niin sen jälkeen arvostelussa käytetyt tähden muuttuvat uudelleen "tyhjiksi" vaikuttaen siltä, ettei käyttäjä olisikaan arvostellut reseptiä. Arvostelu kylläkin toimii aivan halutulla tavalla, ja jos käyttäjä arvostelee reseptin uudelleen, niin edellinen arvostelu päivittyy uuteen. Myös useammat toiminnallisuudet, kuten reseptien muokkaus, omien reseptien poisto, kommenttien poisto ja kattavampi reseptihaku jäivät toteuttamatta. 
