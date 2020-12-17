import sys
import pytest
import json
import synapseclient
from pathlib import Path
from src import synapsebuilder as sb

relativePath = Path(__file__).parent

def test_jsonIngest(capsys):
    with pytest.raises(SystemExit) as emptyPath_e:
        sb.ingestJSON(relativePath)
    assert emptyPath_e.type == SystemExit
  
    with pytest.raises(SystemExit) as badPath_e:
        sb.ingestJSON(relativePath / './badPath.json')
    assert badPath_e.type == SystemExit
    assert badPath_e.value.args[0] == "Could not find file"

    with pytest.raises(SystemExit) as badFile_e:
        sb.ingestJSON(relativePath / './badproject.json')
    assert badFile_e.type == SystemExit
    assert badFile_e.value.args[0] == "Please provide a valid JSON file"


def test_createProject(capsys):
    with pytest.raises(SystemExit) as noProjectName_e:
        sb.createProject('')
    assert noProjectName_e.type == SystemExit
    assert noProjectName_e.value.args[0] == "Please provide a name."
    
    with pytest.raises(SystemExit) as noneProjectName_e:
        sb.createProject(None)
    assert noneProjectName_e.type == SystemExit
    assert noneProjectName_e.value.args[0] == "Please provide a name."
    
    with pytest.raises(SystemExit) as existingProjectName_e:
        sb.createProject('TREAT_AD_POC')
    assert existingProjectName_e.type == SystemExit
    assert existingProjectName_e.value.args[0] == "Please provide a name that doesn't already exist."

def test_createFolder(capsys):
    # testing names
    with pytest.raises(SystemExit) as noFolderName_e:
        sb.createFolder('', 'syn23643783')
    assert noFolderName_e.type == SystemExit
    assert noFolderName_e.value.args[0] == "Please provide a name for your folder."
    
    with pytest.raises(SystemExit) as noneFolderName_e:
        sb.createFolder(None, 'syn23643783')
    assert noneFolderName_e.type == SystemExit
    assert noneFolderName_e.value.args[0] == "Please provide a name for your folder."
    
    with pytest.raises(SystemExit) as existingFolderName_e:
        sb.createFolder('******///_-+_-%$#', 'syn23643783')
    assert existingFolderName_e.type == SystemExit
    assert existingFolderName_e.value.args[0] == "Please provide a valid name."

    # testing parentIds
    with pytest.raises(SystemExit) as noFolderParent_e:
        sb.createFolder('valid_folder_name', '')
    assert noFolderParent_e.type == SystemExit
    assert noFolderParent_e.value.args[0] == "Please provide a parentId for your folder."
    
    with pytest.raises(SystemExit) as noneFolderParent_e:
        sb.createFolder('valid_folder_name', None)
    assert noneFolderParent_e.type == SystemExit
    assert noneFolderParent_e.value.args[0] == "Please provide a parentId for your folder."
    
    with pytest.raises(SystemExit) as existingFolderParent_e:
        sb.createFolder('valid_folder_name', '******///_-+_-%$#')
    assert existingFolderParent_e.type == SystemExit
    assert existingFolderParent_e.value.args[0] == "Please provide a valid name."

