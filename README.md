# wait-time-for-next-bus
wait time for next bus



# Creating pyenv

```
python -m venv pyenv
source pyenv/bin/activate
```

# Installing libraries

```
pip install -r requirements.txt
```


# Execution

Example usage: 
python3 nextbus.py "METRO Blue line" "Target Field Station Platform 1" "south"
python3 nextbus.py "Route 9" "Hedberg Dr and Greenbrier Rd" "west"


# Description for parameters
Input information requires Bus Route, Bus Stop, Direction

- For Bus Route Information, provide the Description of one of the route from https://svc.metrotransit.org/NexTrip/Routes?format=json
- For Bus Stop Information, provide valid stop information. For example:  from https://svc.metrotransit.org/NexTrip/Stops/901/1?format=json
- For Direction, it can be the anyone from this list: south, north, east and west


# Quick Testing with Sample Output

```
./runscript.sh > output-sample.txt &
# sample output found in output-sample.txt
```

# Run unit testing 
```
python3 -m unittest test_nextbus
```



# Core APIs

Core API 
https://svc.metrotransit.org/NexTrip/Routes?format=json
https://svc.metrotransit.org/NexTrip/Directions/9
https://svc.metrotransit.org/NexTrip/Stops/9/1?format=json
https://svc.metrotransit.org/NexTrip/9/1/HEBE?format=json


# References



