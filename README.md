# wait-time-for-next-bus
wait time for next bus


This script returns the information about the Next Bus wait time in minutes. This scripts depends on external service (https://svc.metrotransit.org/NexTrip)


# Description for parameters
Input information requires Bus Route, Bus Stop, Direction

- For Bus Route Information, provide the Description of one of the route from https://svc.metrotransit.org/NexTrip/Routes?format=json
- For Bus Stop Information, provide valid stop information. For example:  from https://svc.metrotransit.org/NexTrip/Stops/901/1?format=json
- For Direction, it can be the anyone from this list: south, north, east and west


# Core APIs Backend are from External Service

- Routes API : https://svc.metrotransit.org/NexTrip/Routes?format=json
- Directions API : https://svc.metrotransit.org/NexTrip/Directions/9
- Stops API : https://svc.metrotransit.org/NexTrip/Stops/9/1?format=json
- WaitTime API : https://svc.metrotransit.org/NexTrip/9/1/HEBE?format=json



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
```
python3 nextbus.py "METRO Blue line" "Target Field Station Platform 1" "south"
python3 nextbus.py "Route 9" "Hedberg Dr and Greenbrier Rd" "west"
```




# Quick Script Execution with Sample Output


```
./runscript.sh > output-sample.txt &
```

## Output
[output-sample.txt](output-sample.txt)


# Run unit testing 
```
python3 -m unittest test_nextbus
```
## Output of Unit tests
[test-output-sample.txt](test-output-sample.txt)




# References

- https://docs.python.org/3/library/glob.html
- https://docs.python.org/3/library/argparse.html
- https://docs.python.org/3/library/subprocess.html



