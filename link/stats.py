from flask import Blueprint, request, render_template

from link import APP_NAME
from link.db import get_db

stats_bp = Blueprint("stats", __name__, url_prefix=f"/{APP_NAME}/stats")

@stats_bp.route("/", methods=["GET"])
def stats():
    """ Render the stats of the database. """
    db = get_db()
    boards = db.execute("SELECT * FROM board").fetchall()
    groups = db.execute("SELECT * FROM board_group").fetchall()
    return render_template("stats/index.html", boards=boards, groups=groups)
