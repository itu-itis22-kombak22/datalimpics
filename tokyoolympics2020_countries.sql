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
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `country_code` varchar(30) NOT NULL,
  `country_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`country_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES ('AFG','Afghanistan'),('ALB','Albania'),('ALG','Algeria'),('Algeria','Algeria'),('AND','Andorra'),('ANG','Angola'),('ANT','Antigua and Barbuda'),('ARG','Argentina'),('Argentina','Argentina'),('ARM','Armenia'),('Armenia','Armenia'),('ARU','Aruba'),('ASA','American Samoa'),('AUS','Australia'),('Australia','Australia'),('Austria','Austria'),('AUT','Austria'),('AZE','Azerbaijan'),('Azerbaijan','Azerbaijan'),('BAH','Bahamas'),('BAN','Bangladesh'),('BAR','Barbados'),('Barbados','Barbados'),('BDI','Burundi'),('BEL','Belgium'),('Belarus','Belarus'),('Belgium','Belgium'),('BEN','Benin'),('BER','Bermuda'),('BHU','Bhutan'),('BIH','Bosnia and Herzegovina'),('BIZ','Belize'),('BLR','Belarus'),('BOL','Bolivia'),('Bolivia','Bolivia'),('BOT','Botswana'),('BRA','Brazil'),('Brazil','Brazil'),('BRN','Bahrain'),('BRU','Brunei Darussalam'),('BUL','Bulgaria'),('Bulgaria','Bulgaria'),('BUR','Burkina Faso'),('CAF','Central African Republic'),('CAM','Cambodia'),('Cameroon','Cameroon'),('CAN','Canada'),('Canada','Canada'),('CAY','Cayman Islands'),('CGO','Congo'),('CHA','Chad'),('CHI','Chile'),('Chile','Chile'),('Chinese Taipei','Chinese Taipei'),('CHN','People\'s Republic of China'),('CIV','CÃ´te d\'Ivoire'),('CMR','Cameroon'),('COD','Democratic Republic of the Congo'),('COK','Cook Islands'),('COL','Colombia'),('Colombia','Colombia'),('COM','Comoros'),('Costa Rica','Costa Rica'),('CPV','Cape Verde'),('CRC','Costa Rica'),('CRO','Croatia'),('Croatia','Croatia'),('CUB','Cuba'),('Cuba','Cuba'),('CYP','Cyprus'),('CZE','Czech Republic'),('Czech Republic','Czech Republic'),('DEN','Denmark'),('Denmark','Denmark'),('DJI','Djibouti'),('DMA','Dominique'),('DOM','Dominican Republic'),('Dominican Republic','Dominican Republic'),('ECU','Ecuador'),('Ecuador','Ecuador'),('EGY','Egypt'),('Egypt','Egypt'),('El Salvador','El Salvador'),('EOR','EOR'),('ERI','Eritrea'),('ESA','El Salvador'),('ESP','Spain'),('EST','Estonia'),('ETH','Ethiopia'),('Ethiopia','Ethiopia'),('FIJ','Fiji'),('FIN','Finland'),('Finland','Finland'),('FRA','France'),('France','France'),('FSM','Federated States of Micronesia'),('GAB','Gabon'),('Gabon','Gabon'),('GAM','Gambia'),('GBR','Great Britain'),('GBS','Guinea-Bissau'),('GEO','Georgia'),('Georgia','Georgia'),('GEQ','Equatorial Guinea'),('GER','Germany'),('Germany','Germany'),('GHA','Ghana'),('GRE','Greece'),('Great Britain','Great Britain'),('Greece','Greece'),('GRN','Grenada'),('GUA','Guatemala'),('GUI','Guinea'),('Guinea','Guinea'),('GUM','Guam'),('GUY','Guyana'),('HAI','Haiti'),('HKG','Hong Kong, China'),('HON','Honduras'),('Honduras','Honduras'),('Hong Kong, China','Hong Kong, China'),('HUN','Hungary'),('Hungary','Hungary'),('INA','Indonesia'),('IND','India'),('India','India'),('Indonesia','Indonesia'),('Iraq','Iraq'),('Ireland','Ireland'),('IRI','Islamic Republic of Iran'),('IRL','Ireland'),('IRQ','Iraq'),('ISL','Iceland'),('Islamic Republic of Iran','Islamic Republic of Iran'),('ISR','Israel'),('Israel','Israel'),('ISV','Virgin Islands, US'),('ITA','Italy'),('Italy','Italy'),('IVB','Virgin Islands, British'),('JAM','Jamaica'),('Jamaica','Jamaica'),('Japan','Japan'),('JOR','Jordan'),('Jordan','Jordan'),('JPN','Japan'),('KAZ','Kazakhstan'),('Kazakhstan','Kazakhstan'),('KEN','Kenya'),('Kenya','Kenya'),('KGZ','Kyrgyzstan'),('KIR','Kiribati'),('KOR','Republic of Korea'),('KOS','Kosovo'),('KSA','Saudi Arabia'),('KUW','Kuwait'),('Kuwait','Kuwait'),('Kyrgyzstan','Kyrgyzstan'),('LAO','Lao People\'s Democratic Republic'),('LAT','Latvia'),('Latvia','Latvia'),('LBA','Libya'),('LBN','LBN'),('LBR','Liberia'),('LCA','Saint Lucia'),('Lebanon','Lebanon'),('LES','Lesotho'),('Lesotho','Lesotho'),('LIE','Liechtenstein'),('Lithuania','Lithuania'),('LTU','Lithuania'),('LUX','Luxembourg'),('MAD','Madagascar'),('Malawi','Malawi'),('Malaysia','Malaysia'),('MAR','Morocco'),('MAS','Malaysia'),('Mauritania','Mauritania'),('Mauritius','Mauritius'),('MAW','Malawi'),('MDA','Republic of Moldova'),('MDV','Maldives'),('MEX','Mexico'),('Mexico','Mexico'),('MGL','Mongolia'),('MHL','Marshall Islands'),('MKD','North Macedonia'),('MLI','Mali'),('MLT','Malta'),('MNE','Montenegro'),('MON','Monaco'),('Mongolia','Mongolia'),('Montenegro','Montenegro'),('Morocco','Morocco'),('MOZ','Mozambique'),('Mozambique','Mozambique'),('MRI','Mauritius'),('MTN','Mauritania'),('MYA','Myanmar'),('NAM','Namibia'),('NCA','Nicaragua'),('NED','Netherlands'),('NEP','Nepal'),('Netherlands','Netherlands'),('New Zealand','New Zealand'),('NGR','Nigeria'),('NIG','Niger'),('Nigeria','Nigeria'),('NOR','Norway'),('North Macedonia','North Macedonia'),('Norway','Norway'),('NRU','Nauru'),('NZL','New Zealand'),('OMA','Oman'),('Oman','Oman'),('PAK','Pakistan'),('PAN','Panama'),('Panama','Panama'),('PAR','Paraguay'),('People\'s Republic of China','People\'s Republic of China'),('PER','Peru'),('Peru','Peru'),('PHI','Philippines'),('Philippines','Philippines'),('PLE','Palestine'),('PLW','Palau'),('PNG','Papua New Guinea'),('POL','Poland'),('Poland','Poland'),('POR','Portugal'),('Portugal','Portugal'),('PUR','Puerto Rico'),('QAT','Qatar'),('Qatar','Qatar'),('Republic of Korea','Republic of Korea'),('Republic of Moldova','Republic of Moldova'),('ROC','ROC'),('Romania','Romania'),('ROU','Romania'),('RSA','South Africa'),('Russian Federation','Russian Federation'),('RWA','Rwanda'),('Rwanda','Rwanda'),('SAM','Samoa (until 1996 Western Samoa)'),('Saudi Arabia','Saudi Arabia'),('SEN','Senegal'),('Senegal','Senegal'),('Serbia','Serbia'),('SEY','Seychelles'),('Seychelles','Seychelles'),('SGP','Singapore'),('Singapore','Singapore'),('SKN','Saint Kitts and Nevis'),('SLE','Sierra Leone'),('SLO','Slovenia'),('Slovakia','Slovakia'),('Slovenia','Slovenia'),('SMR','San Marino'),('SOL','Solomon Islands'),('SOM','Somalia'),('South Africa','South Africa'),('Spain','Spain'),('SRB','Serbia'),('SRI','Sri Lanka'),('Sri Lanka','Sri Lanka'),('SSD','South Sudan'),('STP','Sao Tome and Principe'),('SUD','Sudan'),('Sudan','Sudan'),('SUI','Switzerland'),('SUR','Suriname'),('Suriname','Suriname'),('SVK','Slovakia'),('SWE','Sweden'),('Sweden','Sweden'),('Switzerland','Switzerland'),('SWZ','Eswatini'),('SYR','Syrian Arab Republic'),('Tajikistan','Tajikistan'),('TAN','United Republic of Tanzania'),('TGA','Tonga'),('THA','Thailand'),('Thailand','Thailand'),('TJK','Tajikistan'),('TKM','Turkmenistan'),('TLS','Timor-Leste'),('TOG','Togo'),('Tonga','Tonga'),('TPE','Chinese Taipei'),('Trinidad and Tobago','Trinidad and Tobago'),('TTO','Trinidad and Tobago'),('TUN','Tunisia'),('Tunisia','Tunisia'),('TUR','Turkey'),('Turkey','Turkey'),('TUV','Tuvalu'),('UAE','United Arab Emirates'),('UGA','Uganda'),('Uganda','Uganda'),('UKR','Ukraine'),('Ukraine','Ukraine'),('United Arab Emirates','United Arab Emirates'),('United States of America','United States of America'),('URU','Uruguay'),('Uruguay','Uruguay'),('USA','United States of America'),('UZB','Uzbekistan'),('Uzbekistan','Uzbekistan'),('VAN','Vanuatu'),('VEN','Venezuela'),('Venezuela','Venezuela'),('VIE','Vietnam'),('VIN','St Vincent and the Grenadines'),('YEM','Yemen'),('ZAM','Zambia'),('ZIM','Zimbabwe'),('Zimbabwe','Zimbabwe');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
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
