import json
import sys
import synapseclient
from synapseclient import Project, Folder, File, Link
from pathlib import Path

#ingest json file into variable
def ingestJSON(filePath):
    try:
        with open(filePath) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
            sys.exit("Could not find file")
    except json.decoder.JSONDecodeError:
            sys.exit("Please provide a valid JSON file")
    except:
            sys.exit("An error has occurred.")


def traverseFolders(current, currentPath=''):
    
    #folder creation happens here
    if current['name']:
        currentPath += '/' + current['name']
        print('create ' + currentPath)
        #create object in Synapse
    
    if 'folders' not in current:
        return


    for i in range(len(current['folders'])):
        traverseFolders(current['folders'][i], currentPath, test)





    '''
    main function
    Steps:
        1 - Attempt to read configuration file.
        2 - Attempt to login with Synapse Credentials
        3 - Attempt to traverse the folder structure while creating folders
    '''
def main():
    relativePath = Path(__file__).parent / sys.argv[1]
    json_data = ingestJSON(relativePath)

    global syn
    syn = synapseclient.Synapse()
    syn.login(rememberMe=True)

    traverseFolders(json_data)


if __name__ == "__main__":
    main()
