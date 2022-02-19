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
  description TEXT,
  prep_time INTEGER
);


-- Adding some recipes into database --
INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time
) VALUES (
  'Mokkapalat',
  'dessert',
  '{3 kananmunaa, 3dl sokeria, 150g voita, 5dl vehnäjauhoja, 3rkl kaakaojauhetta, 2tl leivinjauhetta, 1tl vaniljasokeria, 2dl kahvia, 5rkl kuumaa kahvia, 5rkl margariinia, 4dl tomusokeria, 2tl vaniliinisokeria, 3rkl kaakaojauhetta}',
  'Katso ohje osoitteesta https://www.k-ruoka.fi/reseptit/mokkapalat',
  45
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time
) VALUES (
  'Kalakeitto',
  'maincourse',
  '{8dl vettä, 8 kokonaista maustepippuria, 2 laakerinlehteä, 1-2 sipulia, 750g perunaa, 600g lohta, 1tl suolaa, 2dl ruokakermaa, 1dl tilliä}',
  'Katso ohje osoitteesta https://www.valio.fi/reseptit/kalakeitto/',
  45
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time
) VALUES (
  'Pannari',
  'dessert',
  '{2 kananmunaa, 8dl maitoa, 4dl vehnäjauhoja, 1dl kauraleseitä, 1tl suolaa, 1rkl sokeria, 75g voita}',
  'Katso ohje osoitteesta https://www.valio.fi/reseptit/pannari-1/',
  50
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time
) VALUES (
  'Mangorahkapiirakka',
  'dessert',
  '{175g voita, 3dl vehnäjauhoja, 2dl sokeria, 1.5dl kookoshiutaleita, 2tl vaniljasokeria, 1tl leivinjauhetta, 2 kananmunaa, 1dl maitoa, 1tlk säilykeaprikoosia, 200g mango-passion rahkaa}',
  'Katso ohje osoitteesta https://www.valio.fi/reseptit/mangorahkapiirakka/',
  60
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time
) VALUES (
  'Riisipuuro',
  'other',
  '{1dl vettä, 2dl puuroriisiä, 0.5tl suolaa, 2dl kuohukermaa}',
  'Katso ohje osoitteesta https://www.valio.fi/reseptit/riisipuuro-kermalla/',
  40
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time
) VALUES (
  'Kanaquesadilla',
  'other',
  '{8 vehnätortillaa, 230g salsakastiketta, 200g kypsää broilerifileetä, 1 ruukku korianteria, 150g juustoa}',
  'Katso ohje osoitteesta https://www.valio.fi/reseptit/kanaquesadilla-uunissa/',
  25
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time
) VALUES (
  'Lohta ja pastaa',
  'maincourse',
  '{250g raakaa pastaa, 150g kylmäsavulohta, 125g kirsikkatomaatteja, 2.5dl ruokakermaa, 150g juustoraastetta}',
  'Katso ohje osoitteesta https://www.valio.fi/reseptit/lohta-ja-pastaa/',
  30
);