# synapse-project-builder
Simple tool to create a Synapse project's folder structure from a configuration file

# Usage
<br>From the root folder invoke the script and include the relative path of the configuration file (relative to where the script is):
```bash
python ./src/synapsebuilder.py ../test/goodProject.json
```

# Running Tests
```bash
pytest --capture=sys
```