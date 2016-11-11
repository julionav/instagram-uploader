import json, csv, time
from datetime import datetime, timedelta
from collections import deque

import click
from InstagramAPI import InstagramAPI

'''
Script for uploading videos/images in a specific datetime to instagram from a csv file. In the 
csv file is specified the username, image/video, caption and upload datetime
'''

@click.command()
@click.option('--accounts_file', default='accounts.json', help='Json file that contains the accounts to be used')
@click.option('--photos', default='photos', help='Folder name where are stored the photos')
@click.option('--videos', default='videos', help='Folder name where are stored the videos')
@click.option('--uploads_file', default='uploads.csv', help='Csv file where are the upload tasks')
def instagram_upload(accounts_file, photos, videos, uploads_file):
    # Reading the accounts
    with open(accounts_file, 'r') as a:
        accounts = json.load(a)
        # Dict with pending uploads created using username as key. every username
        # will have a tuple with the pending uploads for that account
        uploads = {}
        for username in accounts.keys():
            uploads[username] = []


    # Reading pending uploads
    with open(uploads_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        now = datetime.today()
        # We cache the content of the csv file to remove later the successful uploads
        csv_rows = []
        for row in reader:
            date_upload = datetime.strptime(row['upload datetime'], '%Y-%m-%d_%H:%M:%S')
            if date_upload < now:
                if row['username'] in uploads:
                    uploads[username].append(row)

                else:
                    print('{} is not in the configured accounts'.format['username'])
            else:
                # Only the files that are not pending for upload are cached.
                # Later the unsuccessful uploads will be readded to the csv file
                csv_rows.append(row)

    # Uploading the files in the queue
    for user_uploading in uploads:
        instagram = InstagramAPI(user_uploading, accounts[user_uploading], debug=True)
        instagram.login()

        for upload in uploads[user_uploading]:
            # To store the uploads that fail
            unsuccessful_uploads = []
            if upload['video']:
                print('Uploading {} to the {} instagram account'.format(upload['video'], user_uploading))
                for i in range(1):
                    # We try 3 times to upload the photo. If it's successful it will remove the upload from the list
                    if instagram.uploadVideo('{}/{}'.format(videos, upload['video']), caption=upload['caption']):
                        print('Successful upload of {} to the {} instagram account'.format(upload['video'], user_uploading))
                        break

                    else:
                        print(instagram.LastJson)
                        unsuccessful_uploads.append(upload)

            else:
                print('Uploading {} to the {} instagram account'.format(upload['photo'], user_uploading))
                for i in range(1):                     
                    # We try 3 times to upload the photo. If it's successful it will remove the upload from the list
                    if instagram.uploadPhoto('{}/{}'.format(photos, upload['photo']), caption=upload['caption']):
                        print('Successful upload of {} to the {} instagram account'.format(upload['photo'], user_uploading))
                        break
    
                else:
                    print(instagram.LastJson)
                    unsuccessful_uploads.append(upload)
                
       

    # Once the pending uploads are ready we re-write the csv file without the successful uploads.
    with open('uploads.csv', 'w') as csvfile:
        fieldnames = ['username', 'photo', 'video', 'caption', 'upload datetime']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()

        # we add the unsuccessful uploads to the csv_rows
        for unsuccessful_upload in unsuccessful_uploads:
            # we add it to the begining of the csvfile
            csv_rows.insert(0, unsuccessful_upload)

        writer.writerows(csv_rows)

if __name__ == '__main__':
    instagram_upload()