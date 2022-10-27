import dbm
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
GCP_MYSQL_HOSTNAME = os.getenv("GCP_MYSQL_HOSTNAME")
GCP_MYSQL_USER = os.getenv("GCP_MYSQL_USERNAME")
GCP_MYSQL_PASSWORD = os.getenv("GCP_MYSQL_PASSWORD")
GCP_MYSQL_DATABASE = os.getenv("GCP_MYSQL_DATABASE")

connection_string_gcp = f'mysql+pymysql://{GCP_MYSQL_USER}:{GCP_MYSQL_PASSWORD}@{GCP_MYSQL_HOSTNAME}:3306/{GCP_MYSQL_DATABASE}'
db_gcp = create_engine(connection_string_gcp)

MYSQL_HOSTNAME = os.getenv('MYSQL_HOSTNAME')
MYSQL_USER = os.getenv('MYSQL_USERNAME')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3305/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

table_Patients = """
create table if not exists patients (
    id int auto_increment,
    mrn varchar(255) default null unique,
    first_name varchar(255) default null,
    last_name varchar(255) default null,
    zip_code varchar(255) default null,
    dob varchar(255) default null,
    gender varchar(255) default null,
    contact_mobile varchar(255) default null,
    contact_home varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""
table_Medications = """
create table if not exists medications (
    id int auto_increment,
    mrn varchar(255) default null,
    med_ndc varchar(255) default null unique,
    med_human_name varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES patients(mrn) ON DELETE CASCADE
); 
"""

table_Treatments_Procedures = """
create table if not exists treatments_procedures (
    id int auto_increment,
    mrn varchar(255) default null,
    CPT_code varchar(255) default null,
    CPT_description varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES patients(mrn) ON DELETE CASCADE
);
"""

table_Conditions = """
create table if not exists patient_conditions (
    id int auto_increment,
    icd10_code varchar(255) default null unique,
    icd10_description varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""

table_SDoH = """
create table if not exists social_determinants(
    id int auto_increment,
    LOINC_NUM varchar(255) default null,
    COMPONENT varchar(255) default null,
    PRIMARY KEY (id)
);
"""
engine.execute(table_Patients)
engine.execute(table_Medications)
engine.execute(table_Treatments_Procedures)
engine.execute(table_Conditions)
engine.execute(table_SDoH)

gcp_tables = db_gcp.table_names()
