import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query_join, query_aggregate, query_sort


def handle_arguments(args):
    """Parse and handle CLI arguments."""
    parser = argparse.ArgumentParser(description="ETL and Query CLI")

    parser.add_argument(
        "action",
        choices=["extract", "transform", "query_join", "query_aggregate", "query_sort"],
        help="Perform: extract data, transform, or queries.",
    )

    return parser.parse_args(args)


def main():
    """Main function to handle CLI commands."""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        result = extract()
        print(result)

    elif args.action == "transform":
        print("Transforming and loading data...")
        result = load()
        print(result)

    elif args.action == "query_join":
        print("Running join query...")
        result = query_join()
        print(result)

    elif args.action == "query_aggregate":
        print("Running aggregate query...")
        result = query_aggregate()
        print(result)

    elif args.action == "query_sort":
        print("Running sort query...")
        result = query_sort()
        print(result)

    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()


# on command line rin "cargo --version"
# On command line type "cargo new temp"
# can add lib.rs

# cargo comes with linter, formatter, tester

# cargo fmt
# cargo clippy
# cargo check
# cargo build

# degub:
# release:

# enum commands..


# main parses and makes connection to sql database

# inside add there is a test
