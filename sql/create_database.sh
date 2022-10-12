#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_USER" <<-EOSQL
	CREATE DATABASE "$DB_NAME";    	
EOSQL


psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$DB_NAME" <<-EOSQL
	CREATE TABLE IF NOT EXISTS "$TB_NAME" (    
        id serial PRIMARY KEY,    
        station_id text,
        bikes_available text,
        docks_available text,
        time timestamp);
EOSQL
