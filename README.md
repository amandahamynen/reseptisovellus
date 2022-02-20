# Reseptisovellus
Sovellus on toteutettu kurssilla Tietokantasovellus (kevät 2022)


https://tsoha-reseptisovellus.herokuapp.com

Sovellusta on mahdollista testata herokussa. Jotta kaikkia toiminnallisuuksia voi kokeilla, tulee sinne ensin luoda oma käyttäjä tai käyttää valmiiksi luotua käyttäjää (käyttäjänimi: testi_käyttäjä, salasana: salasana123).

## Sovelluksen alustava kuvaus
Reseptisovelluksella käyttäjä voi hakea tietokantaan lisättyjä reseptejä. Jos käyttäjä haluaa lisätä tietokantaan itse reseptin, hänen tulee ensin rekisteröityä sovellukseen käyttäjätunnuksella ja salasanalla. Tämän jälkeen hän voi kirjautua kyseisellä tunnuksella sovellukseen, ja lisätä reseptejä. Sivustolla on lisäksi olemassa ylläpitäjä, joka pystyy poistamaan reseptejä (ei vielä toteutettu)
### Ominaisuudet:
Kuka tahansa pystyy...
- [x] rekisteröidä uuden käyttäjän
- [x] kirjautua sisään jo olemassa olevalla käyttäjällä
- hakea reseptejä...
  - [x] reseptin nimen perusteella
  - [ ] ainesosan perusteella
  - [ ] reseptin lisääjän käyttäjänimen perusteella
- lajitella näytettävät reseptit...
  - [x] aakkosjärjestyksen mukaan
  - [x] suosion mukaan
  - [ ] arvosteluiden mukaan
  - [x] lisäysajan mukaan
  - [x] reseptin valmistusajan mukaan
  - [x] ruokalajin perusteella
- nähdä, kuinka monta tykkäystä reseptillä on
  
Kirjautunut käyttäjä pystyy...
- [x] lisätä uuden reseptin
- [x] kirjautua ulos käyttäjältä
- [ ] kommentoimaan muita reseptejä
- [ ] arvostelemaan reseptejä asteikolla 1-5
- [x] lisätä reseptejä omiin suosikkeihin
- [ ] pystyy muokata omia reseptejä
- [x] tykätä reseptistä

Ylläpitäjä pystyy...
- [ ] poistamaan reseptin sivustolta
- [ ] poistamaan kommentteja
- [ ] pystyy poistamaan käyttäjiä
