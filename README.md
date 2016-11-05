# MFG

## setup
pip install -r requirements.txt

create a secret.json modelled after secret.json.sample with actual secrets


## how to run
python hello_webapp/app.py


## alternative
if you don't want to worry about the web app setup,
you can just write receipt printers in receipt_printers
in any language you want
and I can hook them up to the web app later

---

print cmd for the receipt printer on raspberry pi:

    lpr -o -fit-to-page IMAGE.JPG