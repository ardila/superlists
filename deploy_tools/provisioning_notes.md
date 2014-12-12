Provisioning a new site
======================

## Required packages

 * nginx
 * python
 * git
 * pip
 * virtualenv

 eg, on Ubuntu

    sudo apt-get install nginx git python python-pip
    sudo pip install virtualenv

 ## Nginx Virtual Host config
 
 * see nginx.template.conf
 * replace staging.waawwaaw.com with the real name

 ## Upstart Job

 * see gunicon-upstart.template.conf
 * replace staging.waawwaaw.com with, eg, staging.my-domain.com

 ## Folder structure
 /home/username
 └── sites
     └── SITENAME
              ├── database
              ├── source
              ├── static
              └── virtualenv
