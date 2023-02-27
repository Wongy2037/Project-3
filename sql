CREATE TABLE `coviddata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `province` varchar(60) DEFAULT '',
  `country` varchar(60) DEFAULT '',
  `lat` decimal(10,6) DEFAULT NULL,
  `long` decimal(10,6) DEFAULT NULL,
  `data` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=290 DEFAULT CHARSET=utf8
CREATE TABLE `coviddata_death` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `province` varchar(60) DEFAULT '',
  `country` varchar(60) DEFAULT '',
  `lat` decimal(10,6) DEFAULT NULL,
  `long` decimal(10,6) DEFAULT NULL,
  `data` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=290 DEFAULT CHARSET=utf8
CREATE TABLE `coviddata_death_sum` (
  `country` varchar(100) DEFAULT '',
  `data` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8
CREATE TABLE `coviddata_recovered` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `province` varchar(60) DEFAULT '',
  `country` varchar(60) DEFAULT '',
  `lat` decimal(10,6) DEFAULT NULL,
  `long` decimal(10,6) DEFAULT NULL,
  `data` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=275 DEFAULT CHARSET=utf8
CREATE TABLE `coviddata_recovered_sum` (
  `country` varchar(100) DEFAULT '',
  `data` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8
CREATE TABLE `coviddata_sum` (
  `country` varchar(100) DEFAULT '',
  `data` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8
CREATE TABLE `other` (
  `name` varchar(50) NOT NULL DEFAULT '',
  `value` longtext,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
