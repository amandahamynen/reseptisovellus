DROP TABLE users CASCADE;
DROP TABLE recipes CASCADE;
DROP TABLE likes CASCADE;
DROP TABLE favourites CASCADE;
DROP TABLE comments CASCADE;
DROP TABLE ratings CASCADE;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT,
  role INTEGER
);

CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  recipe_name TEXT,
  recipe_type TEXT,
  ingredients TEXT[],
  description TEXT[],
  prep_time INTEGER,
  likes INTEGER,
  visible INTEGER,
  creator INTEGER REFERENCES users
);

CREATE TABLE likes (
  user_id INTEGER REFERENCES users,
  recipe_id INTEGER REFERENCES recipes,
  visible INTEGER
);

CREATE TABLE favourites (
  user_id INTEGER REFERENCES users,
  recipe_id INTEGER REFERENCES recipes,
  visible INTEGER
);

CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  recipe_id INTEGER REFERENCES recipes,
  creator INTEGER REFERENCES users,
  comment TEXT,
  created_at TIMESTAMPTZ,
  visible INTEGER
);

CREATE TABLE ratings (
  id SERIAL PRIMARY KEY,
  recipe_id INTEGER REFERENCES recipes,
  user_id INTEGER REFERENCES users
);

-- Adding admin into database --

INSERT INTO users (
  id,
  username,
  password,
  role
) VALUES (
  0,
  'admin',
  'pbkdf2:sha256:260000$X17NI8wtLcaZwp3i$f95cd915bf672f8075d34a186771178bd8c9992ca7464364139a830504fac954',
  2
);

-- Adding some recipes into database --

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time,
  likes,
  visible,
  creator
) VALUES (
  'Mokkapalat',
  'dessert',
  '{3 kananmunaa, 3dl sokeria, 150g voita, 5dl vehnäjauhoja, 3rkl kaakaojauhetta, 2tl leivinjauhetta, 1tl vaniljasokeria, 2dl kahvia, 5rkl kuumaa kahvia, 5rkl margariinia, 4dl tomusokeria, 2tl vaniliinisokeria, 3rkl kaakaojauhetta}',
  '{Katso ohje osoitteesta https://www.k-ruoka.fi/reseptit/mokkapalat}',
  45,
  0,
  1,
  0
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time,
  likes,
  visible,
  creator
) VALUES (
  'Kalakeitto',
  'maincourse',
  '{8dl vettä, 8 kokonaista maustepippuria, 2 laakerinlehteä, 1-2 sipulia, 750g perunaa, 600g lohta, 1tl suolaa, 2dl ruokakermaa, 1dl tilliä}',
  '{Katso ohje osoitteesta https://www.valio.fi/reseptit/kalakeitto/}',
  45,
  0,
  1,
  0
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time,
  likes,
  visible,
  creator
) VALUES (
  'Pannari',
  'dessert',
  '{2 kananmunaa, 8dl maitoa, 4dl vehnäjauhoja, 1dl kauraleseitä, 1tl suolaa, 1rkl sokeria, 75g voita}',
  '{Katso ohje osoitteesta https://www.valio.fi/reseptit/pannari-1/}',
  50,
  0,
  1,
  0
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time,
  likes,
  visible,
  creator
) VALUES (
  'Mangorahkapiirakka',
  'dessert',
  '{175g voita, 3dl vehnäjauhoja, 2dl sokeria, 1.5dl kookoshiutaleita, 2tl vaniljasokeria, 1tl leivinjauhetta, 2 kananmunaa, 1dl maitoa, 1tlk säilykeaprikoosia, 200g mango-passion rahkaa}',
  '{Katso ohje osoitteesta https://www.valio.fi/reseptit/mangorahkapiirakka/}',
  60,
  0,
  1,
  0
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time,
  likes,
  visible,
  creator
) VALUES (
  'Riisipuuro',
  'other',
  '{1dl vettä, 2dl puuroriisiä, 0.5tl suolaa, 2dl kuohukermaa}',
  '{Katso ohje osoitteesta https://www.valio.fi/reseptit/riisipuuro-kermalla/}',
  40,
  0,
  1,
  0
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time,
  likes,
  visible,
  creator
) VALUES (
  'Kanaquesadilla',
  'other',
  '{8 vehnätortillaa, 230g salsakastiketta, 200g kypsää broilerifileetä, 1 ruukku korianteria, 150g juustoa}',
  '{Katso ohje osoitteesta https://www.valio.fi/reseptit/kanaquesadilla-uunissa/}',
  25,
  0,
  1,
  0
);

INSERT INTO recipes (
  recipe_name,
  recipe_type,
  ingredients,
  description,
  prep_time,
  likes,
  visible,
  creator
) VALUES (
  'Lohta ja pastaa',
  'maincourse',
  '{250g raakaa pastaa, 150g kylmäsavulohta, 125g kirsikkatomaatteja, 2.5dl ruokakermaa, 150g juustoraastetta}',
  '{Katso ohje osoitteesta https://www.valio.fi/reseptit/lohta-ja-pastaa/}',
  30,
  0,
  1,
  0
);