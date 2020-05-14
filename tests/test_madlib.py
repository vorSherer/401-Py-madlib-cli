from madlib_cli.madlib import read_template
from madlib_cli.madlib import madlib_parser
from madlib_cli.madlib import template_merge

def test_read_template():
    actual = read_template("test-short.txt")
    expected = "It worked!\nSo get on with it, {NAME}!"
    assert actual == expected


def test_get_keys():
    pass


def test_madlib_parser():
    pass


def test_template_merge():
    pass
