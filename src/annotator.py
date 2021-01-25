import synapseclient

#login
syn = synapseclient.Synapse()
syn.login(rememberMe=True)

# get a list of ids to be annotated
result = syn.tableQuery("SELECT id FROM syn23751446 WHERE category is NULL")

# recursively get their parent while building the name
def findParents(sID, originalEntity, name=""):
    
    entity = syn.get(sID)
    
    if entity['name'] == 'Genes':
        splitName = name.replace("_Core", "").replace("_", " ").split('/')
        
        toBeAnnotated = syn.get(originalEntity)
        toBeAnnotated['gene'] = splitName[1]
        toBeAnnotated['core'] = splitName[2]
        toBeAnnotated['category'] = splitName[3]
        toBeAnnotated['fileFormat'] = name.split(".")[1]

        toBeAnnotated = syn.store(toBeAnnotated)
        return
    
    findParents(entity['parentId'], originalEntity, name="/" + entity['name'] + name)


[findParents(row[0], row[0]) for row in result]