##Setup
    1. Clone the project
    $ git clone git@github.com:tathanhhai/imageSnapWifi.git

    2. Create virtualenv 
    $ mkvirtualenv some-name-here
    or
    $ virtualenv dir-for-virtenv

    3. Install needed Python packages
    $ pip install -r requirements.txt

##Usage

    $ ./grabber.py -h
    $ ./grabber.py ip.address.of.cam
    $ ./grabber.py ip.address.of.cam --delay 0.3
    $ ./grabber.py ip.address.of.cam --frames 50
    $ ./grabber.py ip.address.of.cam -f 150 -d 0.2
