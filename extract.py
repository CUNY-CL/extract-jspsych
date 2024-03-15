#!/usr/bin/env python
"""Extracts CSV data from HTML files produced by experimental interface."""

import argparse
from os import path

from lxml import etree


def main(args: argparse.Namespace) -> None:
    parser = etree.HTMLParser()
    for source in args.source:
        sink_path = f"{path.splitext(source)[0]}.csv"
        with open(source, "r") as source, open(sink_path, "w") as sink:
            tree = etree.parse(source, parser)
            # Selects the text of the first (and only) <pre> tag with
            # id="jspsych-data-display".
            contents = tree.xpath("//pre[@id='jspsych-data-display']/text()")[
                0
            ]
            print(contents, file=sink, end="")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="+")
    main(parser.parse_args())
