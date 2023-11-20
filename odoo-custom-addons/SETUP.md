Prerequisites

    Access to the command line/terminal with sudo permissions.
    Access to a browser.
    Git installed.
    Pip for Python 3 installed.
    NodeJS installed.

After meeting all the prerequisites, follow the steps below to install Odoo 15 on Ubuntu in a Python virtual environment.

Installing Odoo in a virtual environment creates an isolated system and allows testing of different versions on the same machine.
Step 1: Update Repository

Open the terminal and update the apt repository:

sudo apt update

Wait for the update to finish before proceeding to the next step.
Step 2: Install Odoo Dependencies

Install Odoo dependencies with the following command:

sudo apt install -y build-essential wget python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools node-less libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libjpeg8-dev libopenjp2-7-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev

Make sure there are no typos to avoid missing packages.
odoo install dependencies terminal output

The installation fetches all additional dependencies necessary for Odoo installation.
Step 3: Create Odoo User

Running Odoo as a root user poses a security risk. Create a new system user, group, and home directory named Odoo:

sudo useradd -m -d /opt/odoo -U -r -s /bin/bash odoo

The username can be different if it matches the PostgreSQL user and the configuration file information.
Step 4: Install and Configure PostgreSQL

Odoo uses PostgreSQL as the database. Install PostgreSQL from the official Ubuntu repositories with:

sudo apt install postgresql

install postgresql terminal output

Press Y when prompted to continue. Once the installation finishes, create a Postgres user with the same name from the previous step:

sudo su - postgres -c "createuser -s odoo"

The command creates a user named odoo to manage the database.
Step 5: Install wkhtmltopdf

The wkhtmltopdf set of open source tools helps render HTML pages into PDFs and images for generating reports in various formats.

To download the installer, run:

sudo wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb

wkhtmltopdf download terminal output

The command fetches the Debian package. To install the package, run:

sudo apt install ./wkhtmltox_0.12.5-1.bionic_amd64.deb

install wkhtmltopdf terminal output

Press Y when asked to continue the installation. Wait for the process to complete before continuing.
Step 6: Install and Configure Odoo

To install Odoo, follow the steps below:

1. Switch to the odoo user with the sudo su command:

sudo su - odoo

sudo su - odoo terminal output

2. Clone the Odoo 15 source code from the Git repository:

git clone https://www.github.com/odoo/odoo --depth 1 --branch 15.0 /opt/odoo15/odoo

git clone odoo terminal output

4. Navigate to the odoo directory and create a Python virtual environment for Odoo:

cd /opt/odoo

python3 -m venv odoo-venv

5. Activate the environment with:

source odoo-venv/bin/activate

python venv odoo create and activate terminal output

The environment name shows in the terminal before the user.

5. Install the following requirements for Odoo:

pip3 install wheel

pip3 install wheel terminal output

pip3 install -r odoo/requirements.txt

pip3 install odoo requirements terminal output

Wait for the installation to complete.

6. After this, Odoo requires additional setup and configuration. Deactivate the environment with:

deactivate

7. Create a separate directory for custom addons:

mkdir /opt/odoo/odoo-custom-addons

This directory defines where Odoo searches for modules.

8. Switch back to the sudo user with:

exit

custom odoo addons directory terminal output

9. Create the odoo.conf file using the nano text editor:

sudo nano /etc/odoo.conf

Paste the following contents into the odoo.conf file:

[options]
; Database operations password:
admin_passwd = PASSWORD
db_host = False
db_port = False
db_user = odoo
db_password = False
addons_path = /opt/odoo/odoo/addons,/opt/odoo/odoo-custom-addons

odoo.conf file contents

Change the admin_password field to a secure password for the database. The addons_path field contains the paths to Odoo module locations. Save and close the file.

10. Create the odoo.service file with:

sudo nano /etc/systemd/system/odoo.service

Paste the following contents into the file:

[Unit]
Description=Odoo
Requires=postgresql.service
After=network.target postgresql.service

[Service]
Type=simple
SyslogIdentifier=odoo
PermissionsStartOnly=true
User=odoo
Group=odoo
ExecStart=/opt/odoo/odoo-venv/bin/python3 /opt/odoo/odoo/odoo-bin -c /etc/odoo.conf
StandardOutput=journal+console

[Install]
WantedBy=multi-user.target

odoo.service file contents

The service connects to Odoo through the Python virtual environment and uses the configuration file from the previous step. Save the changes and close the file.

11. Update the service list:

sudo systemctl daemon-reload

The Odoo service is now available.
Step 7: Start and Test Odoo

To start and test Odoo, do the following:

1. Enable the Odoo service on system startup:

sudo systemctl enable --now odoo

2. Check the service status with:

sudo systemctl status odoo