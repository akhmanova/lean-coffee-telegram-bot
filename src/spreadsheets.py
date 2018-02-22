# -*- coding: utf-8 -*-

import os

from __future__ import print_function

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    FLAGS = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    FLAGS = None

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
APPLICATION_NAME = 'Lean Coffee'

# TODO
CLIENT_SECRET_FILE = './client_id.json'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'credentials.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if FLAGS:
            credentials = tools.run_flow(flow, store, FLAGS)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('[INFO] Storing credentials to ' + credential_path)
    return credentials
