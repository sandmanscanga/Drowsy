
# Installation


## Setting Up Local System

In order to install the pip package requirements, on some systems you may need to install the following package on top of your mariadb installation.

```bash

sudo apt install libmariadb-dev

```


## Setting Up Local MySQL Database

Install mysql on your system.

Then run the following commands to set up the database...

```bash

# From a terminal (linux)
sudo mysql -uroot -p

```

Then from inside the mysql shell, run these commands...

```sql

create database vuln;
create user vulnerable@localhost identified by 'insecure';
grant all on vuln.* to vulnerable@localhost;
flush privileges;

```
