CREATE DATABASE IF NOT EXISTS gunning_fog_index;
USE gunning_fog_index;

CREATE TABLE gunningfogindex(
	KAM_KEY INT NOT NULL,
    gfindex FLOAT,
    editedtext VARCHAR(100),
    PRIMARY KEY (KAM_KEY));