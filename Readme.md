# Instructions to run
Install z3, networkx in your current python interpreter

Additionally the inputs to the tool are two json file describing the existing network and the direct routes that were added. see data/example.json, data/exampleRoute.json for formatting.

cd to root folder and
Finally run the tool from the command line as follows.
```bash
python src/dynamicPricing.py "data/example.json" "data/exampleRouteExt.json" "results/example.json"
```
The final Network with the updated prices will be stored in "results/example.json", along with some metrics appended for analysis later. 