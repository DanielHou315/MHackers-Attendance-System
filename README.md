# MHackers-Attendance-System
Michigan Hackers Attendance Tracking Scripts

This is a script created for Michigan Hackers to track attendance of its members. It uses services from Google LLC. and TinyURL LLC. This script could be easily adapted to other 



# Configure Script
## Initial Configuration
1. Make sure you have Python>=3.7.0 installed. Some components of the script may not work if you don't have a compatible Python version. 
2. Clone this repository and go to the directory of this repo.
3. Rename config_template.json to config.json, and fill in the API keys as you go through TinyURL and Google Cloud Configuration listed below. 

## TinyURL Configuration
1. Create a TinyURL account if you don't already have one
2. Register a TinyURL API Token in [Dashboard](https://tinyurl.com/app/settings/api). *Make Sure you give it Create and Update TinyURL Permission*. You will ONLY BE SHOWN API TOKEN ONCE. Make sure you copy the API key and replace the <TINYURL_API_KEY> field in the config.json file. The script will be able to read the config file and use the api token you provided. 

## Google Cloud Configuration
Follow Google's [GCP Setup Guide for Python](https://developers.google.com/forms/api/quickstart/python)

# Script Configuration

3. Run the install.sh script to install a virtual environment within the repository folder and install the required packages. You can view the list of packages used for this script in requirements.txt. The default virtual environment directory is added to the gitignore file, so it won't be uploaded to your choice of git service. You can manually remove that in the .gitignore file if you choose to do so. 

On MacOS or Linux, Run the script by 
```
./install.sh
```

If a script does not have execution permission, run
```
chmod +x install.sh       # or use any other .sh file names
```
this adds execution permission to the script file, if it doesn't already have one

On Windows, this probably works, although not guaranteed: 
```
 bash ./install.sh
```

To verify the install, run 
```
./verify_install.sh
```

4. To run the script to create a new form, run 
```
./new_form.sh
```
This runs the script in the virtual environment created within the repo. When the form is created, the shortened URL will be shown to you in Terminal. If there is an error from either Google or TinyURL, it will display the error message. 

4. To run the script to merge forms (STILL IN DEVELOPMENT), run 
```
./merge_form.sh
```
This runs the script in the virtual environment created within the repo. This script will merge all forms within given Google Drive folder to update attendance numbers in a Master form. 

# Development Plans
- Planning to support other URL shortening services if needed
- Planning to support custom naming schemes via json
