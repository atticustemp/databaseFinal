use final;

create table Users (
	ID int,
    fName varchar(255),
    lName varchar(255),
    budget varchar(255),
    state varchar(255),
    industry varchar(255),
    bType varchar(255),
    PRIMARY KEY (ID)
);

create table BType (
	name varchar(255),
    description varchar(255),
    PRIMARY KEY (name)
);

create table Industry (
	name varchar(255),
    marketDescription varchar(255),
    PRIMARY KEY (name)
);

create table Certifications (
	ID int,
	cost int,
    link varchar(255),
    expiration datetime,
    processingTime time,
    department varchar(255),
    cName varchar(255),
    PRIMARY KEY (ID)
);

create table necCert (
	state varchar(255),
    cert varchar(255),
    PRIMARY KEY(state,cert)
);

create table certDependencies (
	cert varchar(255),
    preReq varchar(255),
    PRIMARY KEY(cert,preReq)
);

create table TaxResources (
	url varchar(255),
    state varchar(255),
    resType varchar(255),
    bType varchar(255),
    cost int,
    PRIMARY KEY (url)
);

create table BankingResources (
	url varchar(255),
    state varchar(255),
    resType varchar(255),
    bType varchar(255),
    cost int,
    PRIMARY KEY (url)
);

create table LegalResources (
	url varchar(255),
    state varchar(255),
    resType varchar(255),
    cost int,
    budget varchar(255),
    PRIMARY KEY (url)
);

create table PatentResources (
	url varchar(255),
    resType varchar(255),
    industry varchar(255),
    cost int,
    PRIMARY KEY (url)
);

create table OtherResources (
	url varchar(255),
    state varchar(255),
    resType varchar(255),
    bType varchar(255),
    industry varchar(255),
    cost int,
    PRIMARY KEY (url)
);







    