import sys


def color(text, color):
    if color == "blue":
        color = "0;34m"
    elif color == "green":
        color = "0;32m"
    elif color == "red":
        color = "0;31m"
    elif color == "yellow":
        color = "0;33m"
    else:
        return text
    return "\033[%s%s\033[0m\n" % (color, text)


class NotALogger(object):
    def info(self, msg):
        sys.stdout.write(
            color(msg, "blue")
        )

    def error(self, msg):
        sys.stdout.write(
            color(msg, "red")
        )

    def warning(self, msg):
        sys.stdout.write(
            color(msg, "yellow")
        )

    def success(self, msg):
        sys.stdout.write(
            color(msg, "green")
        )

    def header(self):
        msg = "=" * 50
        msg += "\n" + "=" + (" " * 48) + "="
        msg += "\n" + "=" + (" " * 48) + "="
        msg += "\n" + ("=" * 50)
        sys.stdout.write(
            color(msg, "green")
        )

    def line(self):
        sys.stdout.write(
            color("-" * 50, "blue")
        )


log = NotALogger()

__all__ = ["log"]
