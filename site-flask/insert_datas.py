import sqlite3
def insert_db_datas():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Insert data into table: countries
    countries_data = [
        ('AFG', 'Afghanistan'), ('ALB', 'Albania'), ('ALG', 'Algeria'), ('Algeria', 'Algeria'),
        ('AND', 'Andorra'), ('ANG', 'Angola'), ('ANT', 'Antigua and Barbuda'), ('ARG', 'Argentina'),
        ('Argentina', 'Argentina'), ('ARM', 'Armenia'), ('Armenia', 'Armenia'), ('ARU', 'Aruba'),
        ('ASA', 'American Samoa'), ('AUS', 'Australia'), ('Australia', 'Australia'), ('Austria', 'Austria'),
        ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('Azerbaijan', 'Azerbaijan'), ('BAH', 'Bahamas'),
        ('BAN', 'Bangladesh'), ('BAR', 'Barbados'), ('Barbados', 'Barbados'), ('BDI', 'Burundi'),
        ('BEL', 'Belgium'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('BEN', 'Benin'),
        ('BER', 'Bermuda'), ('BHU', 'Bhutan'), ('BIH', 'Bosnia and Herzegovina'), ('BIZ', 'Belize'),
        ('BLR', 'Belarus'), ('BOL', 'Bolivia'), ('Bolivia', 'Bolivia'), ('BOT', 'Botswana'),
        ('BRA', 'Brazil'), ('Brazil', 'Brazil'), ('BRN', 'Bahrain'), ('BRU', 'Brunei Darussalam'),
        ('BUL', 'Bulgaria'), ('Bulgaria', 'Bulgaria'), ('BUR', 'Burkina Faso'), ('CAF', 'Central African Republic'),
        ('CAM', 'Cambodia'), ('Cameroon', 'Cameroon'), ('CAN', 'Canada'), ('Canada', 'Canada'),
        ('CAY', 'Cayman Islands'), ('CGO', 'Congo'), ('CHA', 'Chad'), ('CHI', 'Chile'),
        ('Chile', 'Chile'), ('Chinese Taipei', 'Chinese Taipei'), ('CHN', 'People\'s Republic of China'),
        ('CIV', 'Côte d\'Ivoire'), ('CMR', 'Cameroon'), ('COD', 'Democratic Republic of the Congo'),
        ('COK', 'Cook Islands'), ('COL', 'Colombia'), ('Colombia', 'Colombia'), ('COM', 'Comoros'),
        ('Costa Rica', 'Costa Rica'), ('CPV', 'Cape Verde'), ('CRC', 'Costa Rica'), ('CRO', 'Croatia'),
        ('Croatia', 'Croatia'), ('CUB', 'Cuba'), ('Cuba', 'Cuba'), ('CYP', 'Cyprus'),
        ('CZE', 'Czech Republic'), ('Czech Republic', 'Czech Republic'), ('DEN', 'Denmark'),
        ('Denmark', 'Denmark'), ('DJI', 'Djibouti'), ('DMA', 'Dominique'), ('DOM', 'Dominican Republic'),
        ('Dominican Republic', 'Dominican Republic'), ('ECU', 'Ecuador'), ('Ecuador', 'Ecuador'),
        ('EGY', 'Egypt'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('EOR', 'EOR'),
        ('ERI', 'Eritrea'), ('ESA', 'El Salvador'), ('ESP', 'Spain'), ('EST', 'Estonia'),
        ('ETH', 'Ethiopia'), ('Ethiopia', 'Ethiopia'), ('FIJ', 'Fiji'), ('FIN', 'Finland'),
        ('Finland', 'Finland'), ('FRA', 'France'), ('France', 'France'), ('FSM', 'Federated States of Micronesia'),
        ('GAB', 'Gabon'), ('Gabon', 'Gabon'), ('GAM', 'Gambia'), ('GBR', 'Great Britain'),
        ('GBS', 'Guinea-Bissau'), ('GEO', 'Georgia'), ('Georgia', 'Georgia'), ('GEQ', 'Equatorial Guinea'),
        ('GER', 'Germany'), ('Germany', 'Germany'), ('GHA', 'Ghana'), ('GRE', 'Greece'),
        ('Great Britain', 'Great Britain'), ('Greece', 'Greece'), ('GRN', 'Grenada'), ('GUA', 'Guatemala'),
        ('GUI', 'Guinea'), ('Guinea', 'Guinea'), ('GUM', 'Guam'), ('GUY', 'Guyana'),
        ('HAI', 'Haiti'), ('HKG', 'Hong Kong, China'), ('HON', 'Honduras'), ('Honduras', 'Honduras'),
        ('Hong Kong, China', 'Hong Kong, China'), ('HUN', 'Hungary'), ('Hungary', 'Hungary'),
        ('INA', 'Indonesia'), ('IND', 'India'), ('India', 'India'), ('Indonesia', 'Indonesia'),
        ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('IRI', 'Islamic Republic of Iran'),
        ('IRL', 'Ireland'), ('IRQ', 'Iraq'), ('ISL', 'Iceland'), ('Islamic Republic of Iran', 'Islamic Republic of Iran'),
        ('ISR', 'Israel'), ('Israel', 'Israel'), ('ISV', 'Virgin Islands, US'), ('ITA', 'Italy'),
        ('Italy', 'Italy'), ('IVB', 'Virgin Islands, British'), ('JAM', 'Jamaica'), ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'), ('JOR', 'Jordan'), ('Jordan', 'Jordan'), ('JPN', 'Japan'),
        ('KAZ', 'Kazakhstan'), ('Kazakhstan', 'Kazakhstan'), ('KEN', 'Kenya'), ('Kenya', 'Kenya'),
        ('KGZ', 'Kyrgyzstan'), ('KIR', 'Kiribati'), ('KOR', 'Republic of Korea'), ('KOS', 'Kosovo'),
        ('KSA', 'Saudi Arabia'), ('KUW', 'Kuwait'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'),
        ('LAO', 'Lao People\'s Democratic Republic'), ('LAT', 'Latvia'), ('Latvia', 'Latvia'),
        ('LBA', 'Libya'), ('LBN', 'LBN'), ('LBR', 'Liberia'), ('LCA', 'Saint Lucia'),
        ('Lebanon', 'Lebanon'), ('LES', 'Lesotho'), ('Lesotho', 'Lesotho'), ('LIE', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('MAD', 'Madagascar'),
        ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('MAR', 'Morocco'), ('MAS', 'Malaysia'),
        ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('MAW', 'Malawi'), ('MDA', 'Republic of Moldova'),
        ('MDV', 'Maldives'), ('MEX', 'Mexico'), ('Mexico', 'Mexico'), ('MGL', 'Mongolia'),
        ('MHL', 'Marshall Islands'), ('MKD', 'North Macedonia'), ('MLI', 'Mali'), ('MLT', 'Malta'),
        ('MNE', 'Montenegro'), ('MON', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'),
        ('Morocco', 'Morocco'), ('MOZ', 'Mozambique'), ('Mozambique', 'Mozambique'), ('MRI', 'Mauritius'),
        ('MTN', 'Mauritania'), ('MYA', 'Myanmar'), ('NAM', 'Namibia'), ('NCA', 'Nicaragua'),
        ('NED', 'Netherlands'), ('NEP', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'),
        ('NGR', 'Nigeria'), ('NIG', 'Niger'), ('Nigeria', 'Nigeria'), ('NOR', 'Norway'),
        ('North Macedonia', 'North Macedonia'), ('Norway', 'Norway'), ('NRU', 'Nauru'), ('NZL', 'New Zealand'),
        ('OMA', 'Oman'), ('Oman', 'Oman'), ('PAK', 'Pakistan'), ('PAN', 'Panama'),
        ('Panama', 'Panama'), ('PAR', 'Paraguay'), ('People\'s Republic of China', 'People\'s Republic of China'),
        ('PER', 'Peru'), ('Peru', 'Peru'), ('PHI', 'Philippines'), ('Philippines', 'Philippines'),
        ('PLE', 'Palestine'), ('PLW', 'Palau'), ('PNG', 'Papua New Guinea'), ('POL', 'Poland'),
        ('Poland', 'Poland'), ('POR', 'Portugal'), ('Portugal', 'Portugal'), ('PUR', 'Puerto Rico'),
        ('QAT', 'Qatar'), ('Qatar', 'Qatar'), ('Republic of Korea', 'Republic of Korea'),
        ('Republic of Moldova', 'Republic of Moldova'), ('ROC', 'ROC'), ('Romania', 'Romania'),
        ('ROU', 'Romania'), ('RSA', 'South Africa'), ('Russian Federation', 'Russian Federation'),
        ('RWA', 'Rwanda'), ('Rwanda', 'Rwanda'), ('SAM', 'Samoa (until 1996 Western Samoa)'),
        ('Saudi Arabia', 'Saudi Arabia'), ('SEN', 'Senegal'), ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'), ('SEY', 'Seychelles'), ('Seychelles', 'Seychelles'), ('SGP', 'Singapore'),
        ('Singapore', 'Singapore'), ('SKN', 'Saint Kitts and Nevis'), ('SLE', 'Sierra Leone'),
        ('SLO', 'Slovenia'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('SMR', 'San Marino'),
        ('SOL', 'Solomon Islands'), ('SOM', 'Somalia'), ('South Africa', 'South Africa'),
        ('Spain', 'Spain'), ('SRB', 'Serbia'), ('SRI', 'Sri Lanka'), ('Sri Lanka', 'Sri Lanka'),
        ('SSD', 'South Sudan'), ('STP', 'Sao Tome and Principe'), ('SUD', 'Sudan'),
        ('Sudan', 'Sudan'), ('SUI', 'Switzerland'), ('SUR', 'Suriname'), ('Suriname', 'Suriname'),
        ('SVK', 'Slovakia'), ('SWE', 'Sweden'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'),
        ('SWZ', 'Eswatini'), ('SYR', 'Syrian Arab Republic'), ('Tajikistan', 'Tajikistan'),
        ('TAN', 'United Republic of Tanzania'), ('TGA', 'Tonga'), ('THA', 'Thailand'),
        ('Thailand', 'Thailand'), ('TJK', 'Tajikistan'), ('TKM', 'Turkmenistan'), ('TLS', 'Timor-Leste'),
        ('TOG', 'Togo'), ('Tonga', 'Tonga'), ('TPE', 'Chinese Taipei'), ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('Tunisia', 'Tunisia'),
        ('TUR', 'Turkey'), ('Turkey', 'Turkey'), ('TUV', 'Tuvalu'), ('UAE', 'United Arab Emirates'),
        ('UGA', 'Uganda'), ('Uganda', 'Uganda'), ('UKR', 'Ukraine'), ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'), ('United States of America', 'United States of America'),
        ('URU', 'Uruguay'), ('Uruguay', 'Uruguay'), ('USA', 'United States of America'),
        ('UZB', 'Uzbekistan'), ('Uzbekistan', 'Uzbekistan'), ('VAN', 'Vanuatu'), ('VEN', 'Venezuela'),
        ('Venezuela', 'Venezuela'), ('VIE', 'Vietnam'), ('VIN', 'St Vincent and the Grenadines'),
        ('YEM', 'Yemen'), ('ZAM', 'Zambia'), ('ZIM', 'Zimbabwe'), ('Zimbabwe', 'Zimbabwe')
    ]

    for country_code, country_name in countries_data:
        cursor.execute("INSERT INTO countries (country_code, country_name) VALUES (?, ?)", (country_code, country_name))
    conn.commit()
    print("countries data inserted successfully")

    # Insert data into table: medals_total
    medals_data = [
        (72,'ARG',0,1,2,3,'Argentina'), (69,'ARM',0,2,2,4,'Armenia'), (6,'AUS',17,7,22,46,'Australia'), 
        (53,'AUT',1,1,5,7,'Austria'), (67,'AZE',0,3,4,7,'Azerbaijan'), (42,'BAH',2,0,0,2,'Bahamas'), 
        (29,'BEL',3,1,3,7,'Belgium'), (63,'BER',1,0,0,1,'Bermuda'), (45,'BLR',1,3,3,7,'Belarus'), 
        (86,'BOT',0,0,1,1,'Botswana'), (12,'BRA',7,6,8,21,'Brazil'), (77,'BRN',0,1,0,1,'Bahrain'), 
        (30,'BUL',3,1,2,6,'Bulgaria'), (87,'BUR',0,0,1,1,'Burkina Faso'), (11,'CAN',7,6,11,24,'Canada'), 
        (2,'CHN',38,32,18,88,'People\'s Republic of China'), (88,'CIV',0,0,1,1,'Côte d\'Ivoire'), 
        (66,'COL',0,4,1,5,'Colombia'), (26,'CRO',3,3,2,8,'Croatia'), (14,'CUB',7,3,5,15,'Cuba'), 
        (18,'CZE',4,4,3,11,'Czech Republic'), (25,'DEN',3,4,4,11,'Denmark'), (68,'DOM',0,3,2,5,'Dominican Republic'), 
        (38,'ECU',2,1,0,3,'Ecuador'), (54,'EGY',1,1,4,6,'Egypt'), (22,'ESP',3,8,6,17,'Spain'), 
        (59,'EST',1,0,1,2,'Estonia'), (56,'ETH',1,1,2,4,'Ethiopia'), (60,'FIJ',1,0,1,2,'Fiji'), 
        (85,'FIN',0,0,2,2,'Finland'), (8,'FRA',10,12,11,33,'France'), (4,'GBR',22,21,22,65,'Great Britain'), 
        (33,'GEO',2,5,1,8,'Georgia'), (9,'GER',10,11,16,37,'Germany'), (89,'GHA',0,0,1,1,'Ghana'), 
        (36,'GRE',2,1,1,4,'Greece'), (90,'GRN',0,0,1,1,'Grenada'), (49,'HKG',1,2,3,6,'Hong Kong, China'), 
        (15,'HUN',6,7,7,20,'Hungary'), (55,'INA',1,1,3,5,'Indonesia'), (48,'IND',1,2,4,7,'India'), 
        (27,'IRI',3,2,2,7,'Islamic Republic of Iran'), (39,'IRL',2,0,2,4,'Ireland'), (40,'ISR',2,0,2,4,'Israel'), 
        (10,'ITA',10,10,20,40,'Italy'), (21,'JAM',4,1,4,9,'Jamaica'), (74,'JOR',0,1,1,2,'Jordan'), 
        (3,'JPN',27,14,17,58,'Japan'), (83,'KAZ',0,0,8,8,'Kazakhstan'), (19,'KEN',4,4,2,10,'Kenya'), 
        (70,'KGZ',0,2,1,3,'Kyrgyzstan'), (16,'KOR',6,4,10,20,'Republic of Korea'), (43,'KOS',2,0,0,2,'Kosovo'), 
        (78,'KSA',0,1,0,1,'Saudi Arabia'), (91,'KUW',0,0,1,1,'Kuwait'), (61,'LAT',1,0,1,2,'Latvia'), 
        (79,'LTU',0,1,0,1,'Lithuania'), (64,'MAR',1,0,0,1,'Morocco'), (75,'MAS',0,1,1,2,'Malaysia'), 
        (92,'MDA',0,0,1,1,'Republic of Moldova'), (84,'MEX',0,0,4,4,'Mexico'), (71,'MGL',0,1,3,4,'Mongolia'), 
        (80,'MKD',0,1,0,1,'North Macedonia'), (81,'NAM',0,1,0,1,'Namibia'), (7,'NED',10,12,14,36,'Netherlands'), 
        (76,'NGR',0,1,1,2,'Nigeria'), (20,'NOR',4,2,2,8,'Norway'), (13,'NZL',7,6,7,20,'New Zealand'), 
        (50,'PHI',1,2,1,4,'Philippines'), (17,'POL',4,5,5,14,'Poland'), (57,'POR',1,1,2,4,'Portugal'), 
        (65,'PUR',1,0,0,1,'Puerto Rico'), (41,'QAT',2,0,1,3,'Qatar'), (5,'ROC',20,28,23,71,'ROC'), 
        (46,'ROU',1,3,0,4,'Romania'), (52,'RSA',1,2,0,3,'South Africa'), (31,'SLO',3,1,1,5,'Slovenia'), 
        (73,'SMR',0,1,2,3,'San Marino'), (28,'SRB',3,1,5,9,'Serbia'), (24,'SUI',3,4,6,13,'Switzerland'), 
        (51,'SVK',1,2,1,4,'Slovakia'), (23,'SWE',3,6,0,9,'Sweden'), (93,'SYR',0,0,1,1,'Syrian Arab Republic'), 
        (62,'THA',1,0,1,2,'Thailand'), (82,'TKM',0,1,0,1,'Turkmenistan'), (34,'TPE',2,4,6,12,'Chinese Taipei'), 
        (58,'TUN',1,1,0,2,'Tunisia'), (35,'TUR',2,2,9,13,'Turkey'), (37,'UGA',2,1,1,4,'Uganda'), 
        (44,'UKR',1,6,12,19,'Ukraine'), (1,'USA',39,41,33,113,'United States of America'), 
        (32,'UZB',3,0,2,5,'Uzbekistan'), (47,'VEN',1,3,0,4,'Venezuela')
    ]

    for medal in medals_data:
        cursor.execute("""
            INSERT INTO medals_total (Rank, Country_Code, Gold_Medal, Silver_Medal, Bronze_Medal, Total, Country) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, medal)
    conn.commit()
    print("medals_total data inserted successfully")
    
    conn.close()