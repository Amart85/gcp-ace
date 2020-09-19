from GSuiteClient import GSuiteClient
from GSuiteUser import GSuiteUser
from GSuiteGroup import GSuiteGroup
    
client = GSuiteClient()
user = GSuiteUser.NewGSuiteUser(
                            "super", 
                            "cooldude", 
                            "SuperSecret1234!@#$", 
                            "supercooldude@elsersmusings.com", 
                            client.DirectoryAPIService)

group = GSuiteGroup.NewGSuiteGroup(
                    "em-supercoolgroup@elsersmusings.com", 
                    "Project Owners for em-supercoolgroup", 
                    "em-supercoolgroup", 
                    client.DirectoryAPIService)

print(f"User {user.name} was created with ID: {user.id}")
print(f"Group {group.name} was created with ID: {group.id}")

group.AddMember(user.id, client.DirectoryAPIService)