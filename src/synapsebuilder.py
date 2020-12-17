import sys
import json
import synapseclient
from synapseclient import Project, Folder
from pathlib import Path


# ingest json file into variable
def ingestJSON(filePath):
    try:
        with open(filePath) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        sys.exit("Could not find file")
    except json.decoder.JSONDecodeError:
        sys.exit("Please provide a valid JSON file")
    except Exception:
        sys.exit("An error has occurred.")


# create project entity in Synapse
def createProject(projectName):

    if projectName == '' or not projectName:
        sys.exit("Please provide a name.")

    project = Project(projectName)

    try:
        project = syn.store(project)
    except Exception:
        sys.exit("Please provide a name that doesn't already exist.")
    return project['id']


# create a single folder entity in Synapse
def createFolder(name, parentId):

    if name == '' or not name:
        sys.exit("Please provide a name for your folder.")

    if parentId == '' or not parentId:
        sys.exit("Please provide a parentId for your folder.")

    data_folder = Folder(name, parent=parentId)

    try:
        data_folder = syn.store(data_folder)
    except Exception:  # empty names will get created named after their synID
        sys.exit("Please provide a valid name.")
    return data_folder['id']


# traverse folder structure while creating project
def traverseFolders(current, parentId, currentPath=''):

    if 'name' in current:
        currentPath += '/' + current['name']

        # create object in Synapse
        parentId = createFolder(current['name'], parentId)

    if 'folders' not in current:  # base case
        return

    for i in range(len(current['folders'])):
        traverseFolders(current['folders'][i], parentId, currentPath)


'''
createProjectStructure function: takes in a path and executes the
following flow:
        1 - Attempt to read configuration file.
        2 - Attempt to login with Synapse Credentials
        3 - Create project
        4 - Attempt to traverse the folder structure while creating folders
'''


def createProjectInSynapse(path):

    projectConfig = ingestJSON(path)

    global syn
    syn = synapseclient.Synapse()
    syn.login(rememberMe=True)

    projectId = createProject(projectConfig['project'])

    traverseFolders(projectConfig, projectId, projectConfig['project'])

    return projectId


def main():
    relativePath = Path(__file__).parent / sys.argv[1]
    createProjectInSynapse(relativePath)


if __name__ == "__main__":
    main()
