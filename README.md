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
  - [ ] suosion mukaan
  - [ ] arvosteluiden mukaan
  - [ ] lisäysajan mukaan
  - [ ] reseptin valmistusajan mukaan
  
Kirjautunut käyttäjä pystyy...
- [x] lisätä uuden reseptin
- [x] kirjautua ulos käyttäjältä
- [ ] kommentoimaan muita reseptejä
- [ ] arvostelemaan reseptejä asteikolla 1-5
- [ ] lisätä reseptejä omiin suosikkeihin
- [ ] pystyy muokata omia reseptejä

Ylläpitäjä pystyy...
- [ ] poistamaan reseptin sivustolta
- [ ] poistamaan kommentteja
- [ ] pystyy poistamaan käyttäjiä
