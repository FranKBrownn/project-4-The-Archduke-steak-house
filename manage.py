#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("ip", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booking.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
