from flask import Blueprint, request
import json

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    # Implement search here!
    filtereUsers = USERS
    dataToSort = []
    position = ("occupation", "age", "name", "id")
    allKeys = set()
    returned_value = []
    # this will get all the keys in the data.
    for user in USERS:
        allKeys.update(user.keys())
    for user in USERS:
        for key, value in args.items():
            if key in allKeys: 
                if str(value).lower() in str(user.get(key)).lower():
                    dataToSort.append(user)
            else:
                return {"message": "Invalid query parameters."}
    # implemnt the sort here
        
    return  dataToSort
