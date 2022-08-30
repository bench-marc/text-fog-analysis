CREATE DATABASE IF NOT EXISTS gunning_fog_index;
USE gunning_fog_index;

DROP TABLE IF EXISTS gunningfogindex;
CREATE TABLE gunningfogindex(
	kam_key INT NOT NULL,
    title VARCHAR(1000),
    description_index FLOAT,
    response_index FLOAT, 
    conclusion_index FLOAT, 
    PRIMARY KEY (kam_key));