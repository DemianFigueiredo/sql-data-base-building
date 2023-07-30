-- How many unique films title are in inventory? From 1000 titles, in the inventory there are 207 film titles.
SELECT COUNT(DISTINCT film_id) AS unique_count
FROM `retro_dvd_vhs`.`inventory`;

-- What are the film titles in the invetory?
SELECT f.title AS Title
FROM `retro_dvd_vhs`.`film` f
JOIN (
    SELECT DISTINCT film_id
    FROM `retro_dvd_vhs`.`inventory`
) i ON f.film_id = i.film_id;


-- How many copys of each movie are in the invetory? 
SELECT film.film_id, film.title AS Title, COUNT(*) AS Copys
FROM retro_dvd_vhs.film
JOIN retro_dvd_vhs.inventory ON film.film_id = inventory.film_id
GROUP BY film.film_id, film.title;

-- How many times a film title has been rented from inventory?
SELECT
    film.film_id AS film_film_id,
    film.title AS title,
    COUNT(rental.rental_id) AS rental_count
FROM
    retro_dvd_vhs.film
JOIN
    retro_dvd_vhs.inventory ON film.film_id = inventory.film_id
LEFT JOIN
    retro_dvd_vhs.rental ON inventory.inventory_id = rental.inventory_id
GROUP BY
    film.film_id, film.title;
   
   -- Top 5 most rented titles 
SELECT
    film.film_id AS film_film_id,
    film.title AS title,
    COUNT(rental.rental_id) AS rental_count
FROM
    retro_dvd_vhs.film
JOIN
    retro_dvd_vhs.inventory ON film.film_id = inventory.film_id
LEFT JOIN
    retro_dvd_vhs.rental ON inventory.inventory_id = rental.inventory_id
GROUP BY
    film.film_id, film.title
ORDER BY
    rental_count DESC
LIMIT 5;
    

