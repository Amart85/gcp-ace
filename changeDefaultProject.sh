#!/bin/bash

echo Welcome to this gcp-ace learning experience. 
echo What is the project name you would like to start managing?
read PROJECTNAME
# Demonstrates command substituion 
gcloud config set project $(gcloud projects list | grep -i $PROJECTNAME | cut -d " " -f1)