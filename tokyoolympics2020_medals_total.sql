-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: tokyoolympics2020
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `medals_total`
--

DROP TABLE IF EXISTS `medals_total`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medals_total` (
  `Rank` int NOT NULL,
  `Country Code` varchar(10) NOT NULL,
  `Gold Medal` int DEFAULT NULL,
  `Silver Medal` int DEFAULT NULL,
  `Bronze Medal` int DEFAULT NULL,
  `Total` int DEFAULT NULL,
  `Country` text,
  PRIMARY KEY (`Country Code`,`Rank`),
  CONSTRAINT `fk_medals_country` FOREIGN KEY (`Country Code`) REFERENCES `countries` (`country_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medals_total`
--

LOCK TABLES `medals_total` WRITE;
/*!40000 ALTER TABLE `medals_total` DISABLE KEYS */;
INSERT INTO `medals_total` VALUES (72,'ARG',0,1,2,3,'Argentina'),(69,'ARM',0,2,2,4,'Armenia'),(6,'AUS',17,7,22,46,'Australia'),(53,'AUT',1,1,5,7,'Austria'),(67,'AZE',0,3,4,7,'Azerbaijan'),(42,'BAH',2,0,0,2,'Bahamas'),(29,'BEL',3,1,3,7,'Belgium'),(63,'BER',1,0,0,1,'Bermuda'),(45,'BLR',1,3,3,7,'Belarus'),(86,'BOT',0,0,1,1,'Botswana'),(12,'BRA',7,6,8,21,'Brazil'),(77,'BRN',0,1,0,1,'Bahrain'),(30,'BUL',3,1,2,6,'Bulgaria'),(87,'BUR',0,0,1,1,'Burkina Faso'),(11,'CAN',7,6,11,24,'Canada'),(2,'CHN',38,32,18,88,'People\'s Republic of China'),(88,'CIV',0,0,1,1,'CÃ´te d\'Ivoire'),(66,'COL',0,4,1,5,'Colombia'),(26,'CRO',3,3,2,8,'Croatia'),(14,'CUB',7,3,5,15,'Cuba'),(18,'CZE',4,4,3,11,'Czech Republic'),(25,'DEN',3,4,4,11,'Denmark'),(68,'DOM',0,3,2,5,'Dominican Republic'),(38,'ECU',2,1,0,3,'Ecuador'),(54,'EGY',1,1,4,6,'Egypt'),(22,'ESP',3,8,6,17,'Spain'),(59,'EST',1,0,1,2,'Estonia'),(56,'ETH',1,1,2,4,'Ethiopia'),(60,'FIJ',1,0,1,2,'Fiji'),(85,'FIN',0,0,2,2,'Finland'),(8,'FRA',10,12,11,33,'France'),(4,'GBR',22,21,22,65,'Great Britain'),(33,'GEO',2,5,1,8,'Georgia'),(9,'GER',10,11,16,37,'Germany'),(89,'GHA',0,0,1,1,'Ghana'),(36,'GRE',2,1,1,4,'Greece'),(90,'GRN',0,0,1,1,'Grenada'),(49,'HKG',1,2,3,6,'Hong Kong, China'),(15,'HUN',6,7,7,20,'Hungary'),(55,'INA',1,1,3,5,'Indonesia'),(48,'IND',1,2,4,7,'India'),(27,'IRI',3,2,2,7,'Islamic Republic of Iran'),(39,'IRL',2,0,2,4,'Ireland'),(40,'ISR',2,0,2,4,'Israel'),(10,'ITA',10,10,20,40,'Italy'),(21,'JAM',4,1,4,9,'Jamaica'),(74,'JOR',0,1,1,2,'Jordan'),(3,'JPN',27,14,17,58,'Japan'),(83,'KAZ',0,0,8,8,'Kazakhstan'),(19,'KEN',4,4,2,10,'Kenya'),(70,'KGZ',0,2,1,3,'Kyrgyzstan'),(16,'KOR',6,4,10,20,'Republic of Korea'),(43,'KOS',2,0,0,2,'Kosovo'),(78,'KSA',0,1,0,1,'Saudi Arabia'),(91,'KUW',0,0,1,1,'Kuwait'),(61,'LAT',1,0,1,2,'Latvia'),(79,'LTU',0,1,0,1,'Lithuania'),(64,'MAR',1,0,0,1,'Morocco'),(75,'MAS',0,1,1,2,'Malaysia'),(92,'MDA',0,0,1,1,'Republic of Moldova'),(84,'MEX',0,0,4,4,'Mexico'),(71,'MGL',0,1,3,4,'Mongolia'),(80,'MKD',0,1,0,1,'North Macedonia'),(81,'NAM',0,1,0,1,'Namibia'),(7,'NED',10,12,14,36,'Netherlands'),(76,'NGR',0,1,1,2,'Nigeria'),(20,'NOR',4,2,2,8,'Norway'),(13,'NZL',7,6,7,20,'New Zealand'),(50,'PHI',1,2,1,4,'Philippines'),(17,'POL',4,5,5,14,'Poland'),(57,'POR',1,1,2,4,'Portugal'),(65,'PUR',1,0,0,1,'Puerto Rico'),(41,'QAT',2,0,1,3,'Qatar'),(5,'ROC',20,28,23,71,'ROC'),(46,'ROU',1,3,0,4,'Romania'),(52,'RSA',1,2,0,3,'South Africa'),(31,'SLO',3,1,1,5,'Slovenia'),(73,'SMR',0,1,2,3,'San Marino'),(28,'SRB',3,1,5,9,'Serbia'),(24,'SUI',3,4,6,13,'Switzerland'),(51,'SVK',1,2,1,4,'Slovakia'),(23,'SWE',3,6,0,9,'Sweden'),(93,'SYR',0,0,1,1,'Syrian Arab Republic'),(62,'THA',1,0,1,2,'Thailand'),(82,'TKM',0,1,0,1,'Turkmenistan'),(34,'TPE',2,4,6,12,'Chinese Taipei'),(58,'TUN',1,1,0,2,'Tunisia'),(35,'TUR',2,2,9,13,'Turkey'),(37,'UGA',2,1,1,4,'Uganda'),(44,'UKR',1,6,12,19,'Ukraine'),(1,'USA',39,41,33,113,'United States of America'),(32,'UZB',3,0,2,5,'Uzbekistan'),(47,'VEN',1,3,0,4,'Venezuela');
/*!40000 ALTER TABLE `medals_total` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-18  0:56:22
