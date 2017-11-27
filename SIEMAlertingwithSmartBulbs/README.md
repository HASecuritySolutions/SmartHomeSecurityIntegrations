# SIEMAlertingwithSmartBulbs

Proof of concept needs the following hardware:

TP-Link 130 Color Smart Bulb

Software required:

Elasticsearch
ElastAlert
Logstash

**Prerequisite**

Install Python code for TPLink

```bash
cd /opt
git clone https://github.com/GadgetReactor/pyHS100
sudo pip install -r requirements.txt
sudo python3 setup.py install
```

For this proof of concept you need to create a folder called rules and place the files ending in .yaml in it. Then configure ElastAlert to use the rules folder.

The files ending in .conf can be used by Logstash to generate proof of concept data.