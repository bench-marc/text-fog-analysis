CREATE DATABASE IF NOT EXISTS gunning_fog_index;
USE gunning_fog_index;

DROP TABLE IF EXISTS gunningfogindex;
CREATE TABLE gunningfogindex(
	kam_key INT NOT NULL,
    title VARCHAR(1000),
	gunning_fog_description_index FLOAT NULL, 
    flesch_reading_description_index FLOAT NULL, 
    gunning_fog_response_index FLOAT NULL, 
    flesch_reading_response_index FLOAT NULL, 
    gunning_fog_conclusion_index FLOAT NULL, 
    flesch_reading_conclusion_index FLOAT NULL, 
    PRIMARY KEY (kam_key));