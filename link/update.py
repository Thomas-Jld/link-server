from flask import Blueprint, request

from link import APP_NAME
from link.db import get_db

update_bp = Blueprint("update", __name__, url_prefix=f"/{APP_NAME}/update")

@update_bp.route("/check", methods=["GET"])
def check():
    return 200

@update_bp.route("/", methods=["GET"])
def update():
    board_id = request.args.get("board_id")
    db = get_db()
    group_id = db.execute(
        "SELECT group_id FROM board WHERE id = ?", (board_id,)
    ).fetchone()[0]

    level = db.execute(
        "SELECT level FROM board_group WHERE id = ?", (group_id,)
    ).fetchone()[0]

    board_count = db.execute(
        "SELECT COUNT(*) FROM board WHERE group_id = ?", (group_id,)
    ).fetchone()[0]

    return {"level": level, "board_count": board_count}
