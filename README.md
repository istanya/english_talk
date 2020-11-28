# English Talk

## Setting up a development environment

We assume that you have `git` and `virtualenv` and `virtualenvwrapper` installed.

    # Clone the code repository into ~/dev/english_talk
    mkdir ~/dev
    cd ~/dev
    git clone https://github.com/istanya/english_talk.git english_talk

    # Create the 'health_project' virtual environment
    mkvirtualenv my-virtualenv --python=python3.7

    # Install required Python packages
    cd ~/dev/english_talk
    workon my-virtualenv
    pip3.7 install -r requirements.txt
    
    # Create data directory 
    # Download https://dropmefiles.com/fB7D7
    # Unzip and locate to data directory 


# Configuring SMTP

Copy the `settings.example.py` file to `settings.py`.

    cp settings.example.py settings.py

Edit the `settings.py` file.


## Initializing the Database

    # Create DB tables and pop  ulate the roles and users tables
    python manage.py init_db


## Running the app

    # Start the Flask development web server
    python manage.py runserver

Point your web browser to http://localhost:5000/
