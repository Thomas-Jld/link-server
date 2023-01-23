from flask import Blueprint, request

from link import APP_NAME
from link.db import get_db

register_bp = Blueprint("register", __name__, url_prefix=f"/{APP_NAME}/register")

@register_bp.route("/", methods=["GET"])
def register():
    """ Register a new board to the general group. """
    board_uid = request.args.get("board_uid")
    db = get_db()
    db.execute(
        "INSERT INTO board (group_id, board_uid) VALUES (1, ?)", (board_uid,)
    )
    db.commit()
    return {"board_id": db.execute("SELECT last_insert_rowid()").fetchone()[0]}
