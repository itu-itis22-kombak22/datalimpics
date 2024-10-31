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
-- Table structure for table `disciplines`
--

DROP TABLE IF EXISTS `disciplines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disciplines` (
  `discipline_id` int NOT NULL AUTO_INCREMENT,
  `discipline_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`discipline_id`),
  UNIQUE KEY `discipline_name` (`discipline_name`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disciplines`
--

LOCK TABLES `disciplines` WRITE;
/*!40000 ALTER TABLE `disciplines` DISABLE KEYS */;
INSERT INTO `disciplines` VALUES (32,''),(45,'3x3 Basketball'),(22,'Archery'),(2,'Artistic Gymnastics'),(26,'Artistic Swimming'),(12,'Athletics'),(24,'Badminton'),(10,'Baseball/Softball'),(4,'Basketball'),(30,'Beach Volleyball'),(21,'Boxing'),(38,'Canoe Slalom'),(14,'Canoe Sprint'),(46,'Cycling BMX Freestyle'),(25,'Cycling BMX Racing'),(44,'Cycling Mountain Bike'),(1,'Cycling Road'),(40,'Cycling Track'),(28,'Diving'),(31,'Equestrian'),(23,'Fencing'),(16,'Football'),(41,'Golf'),(5,'Handball'),(34,'Hockey'),(11,'Judo'),(7,'Karate'),(36,'Marathon Swimming'),(43,'Modern Pentathlon'),(9,'Rhythmic Gymnastics'),(3,'Rowing'),(27,'Rugby Sevens'),(18,'Sailing'),(15,'Shooting'),(42,'Skateboarding'),(47,'Sport Climbing'),(13,'Surfing'),(6,'Swimming'),(17,'Table Tennis'),(20,'Taekwondo'),(39,'Tennis'),(35,'Trampoline Gymnastics'),(37,'Triathlon'),(29,'Volleyball'),(33,'Water Polo'),(19,'Weightlifting'),(8,'Wrestling');
/*!40000 ALTER TABLE `disciplines` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-31 21:47:07
