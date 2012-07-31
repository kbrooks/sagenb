# -*- coding: utf-8 -*
"""
Sage Notebook Storage Abstraction Layer
"""

import os

class Datastore(object):
    """
    The Sage Notebook storage abstraction layer abstract base class.
    Each storage abstraction layer derives from this.
    """
    def __repr__(self):
        """
        String representation of this abstract datastore.

        EXAMPLES::

            sage: from sagenb.storage.abstract_storage import Datastore
            sage: Datastore().__repr__()
            'Abstract Datastore'        
        """
        return "Abstract Datastore"

    def load_server_conf(self):
        raise NotImplementedError
    
    def save_server_conf(self, server_conf):
        raise NotImplementedError

    def load_openid(self):
        raise NotImplementedError
    
    def save_openid(self, openid_dict):
        raise NotImplementedError

    def load_users(self):
        """
        OUTPUT:

            - dictionary of user info
        """
        raise NotImplementedError

    
    def save_users(self, users):
        """
        INPUT:

            - ``users`` -- dictionary mapping user names to users
        """
        raise NotImplementedError

    def load_user_history(self, username):
        """
        Return the history log for the given user.

        INPUT:

            - ``username`` -- string

        OUTPUT:

            - list of strings
        """
        raise NotImplementedError
    
    def save_user_history(self, username, history):
        """
        Save the history log (a list of strings) for the given user.

        INPUT:

            - ``username`` -- string

            - ``history`` -- list of strings
        """
        raise NotImplementedError        
        
    def save_worksheet(self, worksheet, conf_only=False):
        """
        INPUT:

            - ``worksheet`` -- a Sage worksheet

            - ``conf_only`` -- default: False; if True, only save
              the config file, not the actual body of the worksheet      
        """
        raise NotImplementedError        

    def create_worksheet(self, username, id, subpath=None):
        """
        Create worksheet with given id belonging to the given user.

        If the worksheet already exists, return ValueError.

        INPUT:

            - ``username`` -- string

            - ``id`` -- integer

            - ``subpath`` -- string

        OUTPUT:

            - a worksheet
        """
        raise NotImplementedError

    def load_worksheet(self, username, id, subpath = None):
        """
        Return worksheet with given id belonging to the given
        user.

        If the worksheet does not exist, return ValueError.

        INPUT:

            - ``username`` -- string

            - ``id`` -- integer

            - ``subpath`` -- string

        OUTPUT:

            - a worksheet
        """
        raise NotImplementedError        


    def export_worksheet(self, username, id, filename, title, subpath = None):
        """
        Export the worksheet with given username and id to the
        given filename (e.g., 'worksheet.sws').

        INPUT:
    
            - ``title`` - title to use for the exported worksheet (if
               None, just use current title)
        """
        raise NotImplementedError        

    def import_worksheet(self, username, id, filename, subpath = None):
        """
        Input the worksheet username/id from the file with
        given filename.
        """
        raise NotImplementedError        
        
    def worksheets(self, username, subpath = None):
        """
        Return list of all the worksheets, recursively from the directory 
        specified by 'subpath,' belonging to the user with given name.  
        If the given user does not exists, an empty list is returned.

        EXAMPLES: The load_user_data function must be defined in the
        derived class::
        
            sage: from sagenb.storage.abstract_storage import Datastore
            sage: Datastore().worksheets('foobar')
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
        raise NotImplementedError        

        
    def delete(self):
        """
        Delete all files associated with this datastore.  Dangerous!
        This is only here because it is useful for doctesting.
        """
        raise NotImplementedError        
