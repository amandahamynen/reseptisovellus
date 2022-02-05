DROP TABLE users CASCADE;
DROP TABLE recipes CASCADE;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT
);

CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  recipe_name TEXT,
  recipe_type TEXT,
  ingredients TEXT[],
  description TEXT
);


-- Adding some recipes into database --
INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description
) VALUES (
  'Mokkapalat',
  'desert',
  '{3 kananmunaa, 3dl sokeria, 150g voita, 5dl vehnäjauhoja, 3rkl kaakaojauhetta, 2tl leivinjauhetta, 1tl vaniljasokeria, 2dl kahvia}',
  'Vatkaa munat ja sokeri vaahdoksi. Kääntele joukkoon sulatettu, hieman jäähtynyt rasva taikinakaapimella tai puuhaarukalla. Sekoita kuivat aineet keskenään. Lisää ne siivilän läpi vuorotellen kahvin tai maidon kanssa. Vältä turhaa sekoittamista, jotta taikina pysyy kuohkeana eikä sitkisty. Levitä taikina leivinpaperin päälle uunipellille ja paista uunin alatasolla 200 asteessa noin 15 minuuttia. Sulata rasva kuuman kahvin joukkoon. Lisää tomu- ja vanilliinisokeri sekä kaakaojauhe. Levitä pehmeä kuorrute jäähtyneelle piirakkapohjalle. Koristele heti koristerakeilla. Anna kuorrutteen jähmettyä ja leikkaa paloiksi.'
);