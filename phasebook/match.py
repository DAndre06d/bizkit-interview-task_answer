import time
from flask import Blueprint

from .data.match_data import MATCHES

bp = Blueprint("match", __name__, url_prefix="/match")

@bp.route("<int:match_id>")
def match(match_id):
    # the data has length of 4
    # this wil cehck if the user has entered a valid match id
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404
    # this will be responsible for timestamp
    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200

def is_match(fave_numbers_1, fave_numbers_2):
    """
    this function is to cehck if there is a match. this will return a boolean.
    used "set"
    """
    set_fave_numbers_1 = set(fave_numbers_1)
    
    for number in fave_numbers_2:
        if number not in set_fave_numbers_1:
            return False
    
    return True