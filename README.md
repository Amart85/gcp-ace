# Google Cloud Associate Cloud Engineer Certification 
This repo is a collection of my learnings while preparing for the [Google Cloud Associate Cloud Engineer Certification](https://cloud.google.com/certification/cloud-engineer)

## Resources Used
- [Official GCP Certified ACE Study Guide](https://www.amazon.com/Google-Cloud-Certified-Associate-Engineer/dp/1119564417/ref=asc_df_1119564417/?tag=hyprod-20&linkCode=df0&hvadid=343276535408&hvpos=&hvnetw=g&hvrand=13128660645246426920&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9028239&hvtargid=pla-680726527081&psc=1&tag=&ref=&adgrpid=74543737372&hvpone=&hvptwo=&hvadid=343276535408&hvpos=&hvnetw=g&hvrand=13128660645246426920&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9028239&hvtargid=pla-680726527081)
- [gcloud Reference Docs](https://cloud.google.com/sdk/gcloud/reference)
- [Google Cloud Docs](https://cloud.google.com/docs)
- [G Suite Admin SDK](https://developers.google.com/admin-sdk/directory/v1/reference?authuser=2)


## Getting Started
[Getting started with GCP Free Tier](https://cloud.google.com/free). Follow the link and create a gcp account. 

Google provides a checklist for getting started after you create your account. I went ahead and made fictitious users, groups and Organizational Units to better understand permissions and such later on.

## One thing about IAM
[Understand the IAM Model](https://cloud.google.com/iam/docs/overview)
#### The IAM model for access management has three main parts:

- Member. A member can be a Google Account (for end users), a service account (for apps and virtual machines), a Google group, or a G Suite or Cloud Identity domain that can access a resource. The identity of a member is an email address associated with a user, service account, or Google group; or a domain name associated with G Suite or Cloud Identity domains.
- Role. A role is a collection of permissions. Permissions determine what operations are allowed on a resource. When you grant a role to a member, you grant all the permissions that the role contains.
- Policy. The IAM policy binds one or more members to a role. When you want to define who (member) has what type of access (role) on a resource, you create a policy and attach it to the resource.

### In IAM, you grant access to members. Members can be of the following types:

1. Google Account
2. Service account
3. Google group
4. G Suite domain
Cloud Identity domain

### Resource hierarchy
Google Cloud resources are organized hierarchically:

- The organization is the root node in the hierarchy.
- Folders are children of the organization.
- Projects are children of the organization, or of a folder.
- Resources for each service are descendants of projects.

IAM policy inheritance is transitive; in other words, resources inherit policies from the project, which inherit policies from folders, which inherit policies from the organization. Therefore, the organization-level policies also apply at the resource level.

### Python Quickstart for G Suite Admin SDK
This is not necessarily required for gcp-ace but good to know. I learn more by getting my hands dirty.
```bash
sudo apt-get install python3-pip 
python3 -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
### Getting the Quick Start Code to Work 
This example uses OAuth but you can also specify an API Key instead. 
1. Once you get the sdk installed. Create the [python script](./AdminSDK.py).
2. Enable API. For example: one that will allow you to View and manage the provisioning of users on your domain. "Google_Service_Directory"
- Ensure you turn on the following apis for the project
    - Admin SDK					
    - API Discovery Service
3. Setup OAuth landing page.
4. Create OAuth 2.0 Client ID as a *DESKTOP APP*
5. Download secret.json renaming it "credentials.json" and placing it in your current working directory. 
6. Initialize by running [python script](./AdminSDK.py) and authenticating and authorizing
    - This will generate token file. 
7. Safely store token for later retrieval. 

### Understanding the API
[Users List API Call made in example code](https://developers.google.com/admin-sdk/directory/v1/reference/users/list)

### gcloud Command-Line Tool Quickstart
```bash
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-309.0.0-linux-x86_64.tar.gz 
tar -xvzf google-cloud-sdk-309.0.0-linux-x86_64.tar.gz
./google-cloud-sdk/install.sh
# Restart terminal 
gcloud auth login # This will take you through OAUTH flow
gcloud projects list # if you created a project earlier you should see it listed
gcloud compute instances list # list compute instances "VM's"
gcloud functions list # list cloud functions "lambdas"
gcloud projects create help # get help listing command FLAGS 
gcloud projects create --help # For more verbose help
gcloud projects create cli-123456 --name bensfirstproject --folder 587805611271 # Creates project with id cli-123456 and name bensfirstproject in specific folder
```  
#### Create Second Test Project 
1. As Organization Administrator Create another project either from console or cli
```bash
gcloud projects create em-secondproject --name em-secondproject --folder 587805611271 # Creates project within specific folder named em-secondproject
```
2. Add a member to the project owner group by nesting another google group
    - Create Google Group using [Main.py](./Main.py)
    ```python
    group = GSuiteGroup.NewGSuiteGroup(
            "em-supercoolgroup@elsersmusings.com", 
            "Project Owners for em-supercoolgroup", 
            "em-supercoolgroup", 
            client.DirectoryAPIService)
    ```
