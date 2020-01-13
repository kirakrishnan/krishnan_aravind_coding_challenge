Running Traffic Light Simulator(TLS)

== Install pre-requisites ==

python  3.7.2


== Creating and setting up local environment == 

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

These three commands will create a virtual environment .venv, then activate the virtual environment and install all the python libraries needed to run Traffic Light Simulator


== Running the simulator ==

Once the setup is complete run the below command to run the simulator

python TLS.py


== Deactivate ==

After you are done running the simulator, deactivate your virtual environment:

deactivate


== Running the tests ==

Run the below command to run unit tests. Add new tests every time changes are made to code

python tests.py

