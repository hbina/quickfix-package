import argparse
import os
import pathlib
import sys
import os


def execute(cmd: str):
    print("=====================================")
    print(cmd)
    print("=====================================")
    err_code = os.system(cmd)
    assert err_code == 0


def run(tag: str, path_source: str):
    path_build = "/tmp"
    path_doc = os.path.join(path_source, "doc")

    cmd = f"cd {path_doc}; ./document.sh"
    execute(cmd)

    cmd = f"cd {path_source}; ../git2cl > Changelog"
    execute(cmd)

    cmd = f"cd {path_source}; ./bootstrap"
    execute(cmd)

    cmd = f"rm -f quickfix-{tag}.tar.gz"
    execute(cmd)

    cmd = f"tar czvf quickfix-{tag}.tar.gz quickfix"
    execute(cmd)

    cmd = f"cd {path_source}; ./configure --with-python2 --with-python3"
    execute(cmd)

    cmd = f"cd {path_source}; make"
    execute(cmd)

    cmd = f"cd {path_source}; make check"
    execute(cmd)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", type=str, required=True)
    parser.add_argument("--path", type=str, required=True)
    args = parser.parse_args()
    tag = args.tag
    path = args.path
    run(tag, path)


if __name__ == "__main__":
    main()
