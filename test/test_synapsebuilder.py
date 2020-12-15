import sys
import pytest
import json
import synapseclient
from src import synapsebuilder as sb

def test_jsonIngest(capsys):
    with pytest.raises(SystemExit) as emptyPath_e:
        sb.ingestJSON('')
    assert emptyPath_e.type == SystemExit
  
    with pytest.raises(SystemExit) as badPath_e:
        sb.ingestJSON("./badPath.json")
    assert badPath_e.type == SystemExit
    assert badPath_e.value.args[0] == 'Could not find file'

    with pytest.raises(SystemExit) as badFile_e:
        sb.ingestJSON('./badproject.json')
    assert badFile_e.type == SystemExit



def test_traverseFolders(capsys):
    with pytest.raises(SystemExit) as invalidFolders_e:
        json = sb.ingestJSON('./badTraversal.json')
        sb.traverseFolders(json)
    assert invalidFolders_e.type == SystemExit
