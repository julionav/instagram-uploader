# Instagram Uploader
Instagram uploader built using the Instagram-API-python package to interact with instagram.
instagram_uploader uploads files to instagram that are scheduled with a older date in a csv file (default to uploads.json) to a specific account. You can look at [uploads](uploads.csv) to know
the format of the csv file. The accounts are configured in a json file (default to accounts.json), the photos folder default is "photos" and the 
video folder defaults to "videos"

Instagram uploader can upload photos/videos to any account that is configured.

## Installation
You can install this package with pip:

```
pip install git+https://gitlab.com/Julioocz/instagram_uploader
```

## Usage
Instagram uploader is uses a simple cli to interact with the user. It counts with only a command and 4 options. 

options:
- accounts_file', default='accounts.json', help='Json file that contains the accounts to be used'
- photos', default='photos', help='Folder name where are stored the photos'
- videos', default='videos', help='Folder name where are stored the videos'
- uploads_file', default='uploads.csv', help='Csv file where are the upload tasks'

using it:
```
$ instagram_uploader --photos='yourphoto-folder' --videos='yourvideo-folder' --accounts_file='yourAccounts_file.json' --uploads_file='yourCsv_file.csv'

or using the default values:
$ instagram_uploader
```