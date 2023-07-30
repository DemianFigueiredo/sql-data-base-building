-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema retro_dvd_vhs
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema retro_dvd_vhs
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `retro_dvd_vhs` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
-- -----------------------------------------------------
-- Schema publications
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema publications
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `publications` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `retro_dvd_vhs` ;

-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`actor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`actor` (
  `actor_id` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`actor_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`category` (
  `category_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`category_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`store`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`store` (
  `store_id` INT NOT NULL,
  `store_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`store_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`customer` (
  `costumer_id` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `store_id` INT NOT NULL,
  `phone` VARCHAR(16) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `store_store_id` INT NOT NULL,
  PRIMARY KEY (`costumer_id`, `store_store_id`),
  INDEX `fk_customer_store1_idx` (`store_store_id` ASC) VISIBLE,
  CONSTRAINT `fk_customer_store1`
    FOREIGN KEY (`store_store_id`)
    REFERENCES `retro_dvd_vhs`.`store` (`store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`film`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`film` (
  `film_id` INT NOT NULL,
  `title` VARCHAR(60) NOT NULL,
  `description` LONGTEXT NOT NULL,
  `release_year` BIGINT NOT NULL,
  `language_id` INT NOT NULL,
  `rental_duration` INT NOT NULL,
  `rental_price` DOUBLE NOT NULL,
  `length` INT NOT NULL,
  `replacement_cost` DOUBLE NOT NULL,
  `rating` VARCHAR(45) NOT NULL,
  `special_features` VARCHAR(60) NOT NULL,
  `category_category_id` INT NOT NULL,
  PRIMARY KEY (`film_id`, `category_category_id`),
  INDEX `fk_film_category1_idx` (`category_category_id` ASC) VISIBLE,
  CONSTRAINT `fk_film_category1`
    FOREIGN KEY (`category_category_id`)
    REFERENCES `retro_dvd_vhs`.`category` (`category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`hdd`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`hdd` (
  `title` VARCHAR(60) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `release_year` BIGINT NOT NULL,
  `category_id` INT NOT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`inventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`inventory` (
  `inventory_id` INT NOT NULL,
  `film_id` INT NOT NULL,
  `store_id` INT NOT NULL,
  `film_film_id` INT NOT NULL,
  `film_category_category_id` INT NOT NULL,
  `store_store_id` INT NOT NULL,
  PRIMARY KEY (`inventory_id`, `film_film_id`, `film_category_category_id`, `store_store_id`),
  INDEX `fk_inventory_film1_idx` (`film_film_id` ASC, `film_category_category_id` ASC) VISIBLE,
  INDEX `fk_inventory_store1_idx` (`store_store_id` ASC) VISIBLE,
  CONSTRAINT `fk_inventory_film1`
    FOREIGN KEY (`film_film_id` , `film_category_category_id`)
    REFERENCES `retro_dvd_vhs`.`film` (`film_id` , `category_category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_inventory_store1`
    FOREIGN KEY (`store_store_id`)
    REFERENCES `retro_dvd_vhs`.`store` (`store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`language`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`language` (
  `language_id` INT NOT NULL,
  `audio_type` VARCHAR(6) NOT NULL,
  `audio_language` VARCHAR(25) NOT NULL,
  `subtitle_Y/N` VARCHAR(1) NOT NULL,
  `subtitle_language` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`language_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`staff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`staff` (
  `staff_id` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `lasta_name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `hire_date` DATE NOT NULL,
  `store_id` INT NOT NULL,
  `store_store_id` INT NOT NULL,
  PRIMARY KEY (`staff_id`, `store_store_id`),
  INDEX `fk_staff_store1_idx` (`store_store_id` ASC) VISIBLE,
  CONSTRAINT `fk_staff_store1`
    FOREIGN KEY (`store_store_id`)
    REFERENCES `retro_dvd_vhs`.`store` (`store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`rental`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`rental` (
  `rental_id` INT NOT NULL,
  `return_date` DATETIME NOT NULL,
  `rental_date` DATETIME NOT NULL,
  `inventory_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `staff_id` INT NOT NULL,
  `store_store_id` INT NOT NULL,
  `customer_costumer_id` INT NOT NULL,
  `customer_store_store_id` INT NOT NULL,
  `staff_staff_id` INT NOT NULL,
  `staff_store_store_id` INT NOT NULL,
  PRIMARY KEY (`rental_id`, `store_store_id`, `customer_costumer_id`, `customer_store_store_id`, `staff_staff_id`, `staff_store_store_id`),
  INDEX `fk_rental_store1_idx` (`store_store_id` ASC) VISIBLE,
  INDEX `fk_rental_customer1_idx` (`customer_costumer_id` ASC, `customer_store_store_id` ASC) VISIBLE,
  INDEX `fk_rental_staff1_idx` (`staff_staff_id` ASC, `staff_store_store_id` ASC) VISIBLE,
  CONSTRAINT `fk_rental_store1`
    FOREIGN KEY (`store_store_id`)
    REFERENCES `retro_dvd_vhs`.`store` (`store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_rental_customer1`
    FOREIGN KEY (`customer_costumer_id` , `customer_store_store_id`)
    REFERENCES `retro_dvd_vhs`.`customer` (`costumer_id` , `store_store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_rental_staff1`
    FOREIGN KEY (`staff_staff_id` , `staff_store_store_id`)
    REFERENCES `retro_dvd_vhs`.`staff` (`staff_id` , `store_store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`film_has_actor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`film_has_actor` (
  `film_film_id` INT NOT NULL,
  `actor_actor_id` INT NOT NULL,
  PRIMARY KEY (`film_film_id`, `actor_actor_id`),
  INDEX `fk_film_has_actor_actor1_idx` (`actor_actor_id` ASC) VISIBLE,
  INDEX `fk_film_has_actor_film_idx` (`film_film_id` ASC) VISIBLE,
  CONSTRAINT `fk_film_has_actor_film`
    FOREIGN KEY (`film_film_id`)
    REFERENCES `retro_dvd_vhs`.`film` (`film_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_film_has_actor_actor1`
    FOREIGN KEY (`actor_actor_id`)
    REFERENCES `retro_dvd_vhs`.`actor` (`actor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`film_has_language`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`film_has_language` (
  `film_film_id` INT NOT NULL,
  `language_language_id` INT NOT NULL,
  PRIMARY KEY (`film_film_id`, `language_language_id`),
  INDEX `fk_film_has_language_language1_idx` (`language_language_id` ASC) VISIBLE,
  INDEX `fk_film_has_language_film1_idx` (`film_film_id` ASC) VISIBLE,
  CONSTRAINT `fk_film_has_language_film1`
    FOREIGN KEY (`film_film_id`)
    REFERENCES `retro_dvd_vhs`.`film` (`film_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_film_has_language_language1`
    FOREIGN KEY (`language_language_id`)
    REFERENCES `retro_dvd_vhs`.`language` (`language_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `retro_dvd_vhs`.`inventory_has_rental`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retro_dvd_vhs`.`inventory_has_rental` (
  `inventory_inventory_id` INT NOT NULL,
  `inventory_film_film_id` INT NOT NULL,
  `inventory_film_category_category_id` INT NOT NULL,
  `inventory_store_store_id` INT NOT NULL,
  `rental_rental_id` INT NOT NULL,
  `rental_store_store_id` INT NOT NULL,
  `rental_customer_costumer_id` INT NOT NULL,
  `rental_customer_store_store_id` INT NOT NULL,
  `rental_staff_staff_id` INT NOT NULL,
  `rental_staff_store_store_id` INT NOT NULL,
  PRIMARY KEY (`inventory_inventory_id`, `inventory_film_film_id`, `inventory_film_category_category_id`, `inventory_store_store_id`, `rental_rental_id`, `rental_store_store_id`, `rental_customer_costumer_id`, `rental_customer_store_store_id`, `rental_staff_staff_id`, `rental_staff_store_store_id`),
  INDEX `fk_inventory_has_rental_rental1_idx` (`rental_rental_id` ASC, `rental_store_store_id` ASC, `rental_customer_costumer_id` ASC, `rental_customer_store_store_id` ASC, `rental_staff_staff_id` ASC, `rental_staff_store_store_id` ASC) VISIBLE,
  INDEX `fk_inventory_has_rental_inventory1_idx` (`inventory_inventory_id` ASC, `inventory_film_film_id` ASC, `inventory_film_category_category_id` ASC, `inventory_store_store_id` ASC) VISIBLE,
  CONSTRAINT `fk_inventory_has_rental_inventory1`
    FOREIGN KEY (`inventory_inventory_id` , `inventory_film_film_id` , `inventory_film_category_category_id` , `inventory_store_store_id`)
    REFERENCES `retro_dvd_vhs`.`inventory` (`inventory_id` , `film_film_id` , `film_category_category_id` , `store_store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_inventory_has_rental_rental1`
    FOREIGN KEY (`rental_rental_id` , `rental_store_store_id` , `rental_customer_costumer_id` , `rental_customer_store_store_id` , `rental_staff_staff_id` , `rental_staff_store_store_id`)
    REFERENCES `retro_dvd_vhs`.`rental` (`rental_id` , `store_store_id` , `customer_costumer_id` , `customer_store_store_id` , `staff_staff_id` , `staff_store_store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `publications` ;

-- -----------------------------------------------------
-- Table `publications`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`authors` (
  `au_id` VARCHAR(11) NOT NULL,
  `au_lname` VARCHAR(40) NOT NULL,
  `au_fname` VARCHAR(20) NOT NULL,
  `phone` CHAR(12) NOT NULL,
  `address` VARCHAR(40) NULL DEFAULT NULL,
  `city` VARCHAR(20) NULL DEFAULT NULL,
  `state` CHAR(2) NULL DEFAULT NULL,
  `zip` CHAR(5) NULL DEFAULT NULL,
  `contract` TINYINT NOT NULL,
  PRIMARY KEY (`au_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `publications`.`stores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`stores` (
  `stor_id` CHAR(4) NOT NULL,
  `stor_name` VARCHAR(40) NULL DEFAULT NULL,
  `stor_address` VARCHAR(40) NULL DEFAULT NULL,
  `city` VARCHAR(20) NULL DEFAULT NULL,
  `state` CHAR(2) NULL DEFAULT NULL,
  `zip` CHAR(5) NULL DEFAULT NULL,
  PRIMARY KEY (`stor_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `publications`.`discounts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`discounts` (
  `discounttype` VARCHAR(40) NOT NULL,
  `stor_id` CHAR(4) NULL DEFAULT NULL,
  `lowqty` SMALLINT NULL DEFAULT NULL,
  `highqty` SMALLINT NULL DEFAULT NULL,
  `discount` DECIMAL(4,2) NOT NULL,
  INDEX `discounts_stor_id` (`stor_id` ASC) VISIBLE,
  CONSTRAINT `discounts_ibfk_1`
    FOREIGN KEY (`stor_id`)
    REFERENCES `publications`.`stores` (`stor_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `publications`.`jobs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`jobs` (
  `job_id` SMALLINT NOT NULL,
  `job_desc` VARCHAR(50) NOT NULL,
  `min_lvl` SMALLINT NOT NULL,
  `max_lvl` SMALLINT NOT NULL,
  PRIMARY KEY (`job_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `publications`.`publishers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`publishers` (
  `pub_id` CHAR(4) NOT NULL,
  `pub_name` VARCHAR(40) NULL DEFAULT NULL,
  `city` VARCHAR(20) NULL DEFAULT NULL,
  `state` CHAR(2) NULL DEFAULT NULL,
  `country` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`pub_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `publications`.`employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`employee` (
  `emp_id` CHAR(9) NOT NULL,
  `fname` VARCHAR(20) NOT NULL,
  `minit` CHAR(1) NULL DEFAULT NULL,
  `lname` VARCHAR(30) NOT NULL,
  `job_id` SMALLINT NOT NULL,
  `job_lvl` SMALLINT NULL DEFAULT NULL,
  `pub_id` CHAR(4) NOT NULL,
  `hire_date` DATETIME NOT NULL,
  PRIMARY KEY (`emp_id`),
  INDEX `employee_job_id` (`job_id` ASC) VISIBLE,
  INDEX `employee_pub_id` (`pub_id` ASC) VISIBLE,
  CONSTRAINT `employee_ibfk_1`
    FOREIGN KEY (`job_id`)
    REFERENCES `publications`.`jobs` (`job_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `employee_ibfk_2`
    FOREIGN KEY (`pub_id`)
    REFERENCES `publications`.`publishers` (`pub_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `publications`.`most_profiting_author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`most_profiting_author` (
  `Author ID` VARCHAR(11) CHARACTER SET 'utf8mb3' NOT NULL,
  `Total Profit` DECIMAL(65,8) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `publications`.`most_profiting_authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`most_profiting_authors` (
  `Author ID` VARCHAR(11) CHARACTER SET 'utf8mb3' NOT NULL,
  `Total Profit` DECIMAL(65,8) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `publications`.`pub_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`pub_info` (
  `pub_id` CHAR(4) NOT NULL,
  `logo` LONGBLOB NULL DEFAULT NULL,
  `pr_info` LONGTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`pub_id`),
  CONSTRAINT `pub_info_ibfk_1`
    FOREIGN KEY (`pub_id`)
    REFERENCES `publications`.`publishers` (`pub_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `publications`.`titles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`titles` (
  `title_id` VARCHAR(6) NOT NULL,
  `title` VARCHAR(80) NOT NULL,
  `type` CHAR(12) NOT NULL,
  `pub_id` CHAR(4) NULL DEFAULT NULL,
  `price` DECIMAL(19,4) NULL DEFAULT NULL,
  `advance` DECIMAL(19,4) NULL DEFAULT NULL,
  `royalty` INT NULL DEFAULT NULL,
  `ytd_sales` INT NULL DEFAULT NULL,
  `notes` VARCHAR(200) NULL DEFAULT NULL,
  `pubdate` DATETIME NOT NULL,
  PRIMARY KEY (`title_id`),
  INDEX `titles_pub_id` (`pub_id` ASC) VISIBLE,
  CONSTRAINT `titles_ibfk_1`
    FOREIGN KEY (`pub_id`)
    REFERENCES `publications`.`publishers` (`pub_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `publications`.`roysched`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`roysched` (
  `title_id` VARCHAR(6) NOT NULL,
  `lorange` INT NULL DEFAULT NULL,
  `hirange` INT NULL DEFAULT NULL,
  `royalty` INT NULL DEFAULT NULL,
  INDEX `roysched_title_id` (`title_id` ASC) VISIBLE,
  CONSTRAINT `roysched_ibfk_1`
    FOREIGN KEY (`title_id`)
    REFERENCES `publications`.`titles` (`title_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `publications`.`sales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`sales` (
  `stor_id` CHAR(4) NOT NULL,
  `ord_num` VARCHAR(20) NOT NULL,
  `ord_date` DATETIME NOT NULL,
  `qty` SMALLINT NOT NULL,
  `payterms` VARCHAR(12) NOT NULL,
  `title_id` VARCHAR(6) NOT NULL,
  PRIMARY KEY (`stor_id`, `ord_num`, `title_id`),
  INDEX `sales_title_id` (`title_id` ASC) VISIBLE,
  CONSTRAINT `sales_ibfk_1`
    FOREIGN KEY (`stor_id`)
    REFERENCES `publications`.`stores` (`stor_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `sales_ibfk_2`
    FOREIGN KEY (`title_id`)
    REFERENCES `publications`.`titles` (`title_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `publications`.`titleauthor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publications`.`titleauthor` (
  `au_id` VARCHAR(11) NOT NULL,
  `title_id` VARCHAR(6) NOT NULL,
  `au_ord` TINYINT NULL DEFAULT NULL,
  `royaltyper` INT NULL DEFAULT NULL,
  PRIMARY KEY (`au_id`, `title_id`),
  INDEX `titleauthor_title_id` (`title_id` ASC) VISIBLE,
  CONSTRAINT `titleauthor_ibfk_1`
    FOREIGN KEY (`title_id`)
    REFERENCES `publications`.`titles` (`title_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `titleauthor_ibfk_2`
    FOREIGN KEY (`au_id`)
    REFERENCES `publications`.`authors` (`au_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
