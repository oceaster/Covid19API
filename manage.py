# IMPORTS
import pytest

# RELATIVE IMPORTS
from os import system, environ
from sys import argv, executable
from covid19.settings import BASE_DIR


def main():
    environ.setdefault('DJANGO_SETTINGS_MODULE', 'covid19.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(argv)


def server(start=True, migrate=False):
    def run(_cmd):
        system("{python} {dir}/manage.py {command}".\
            format(python=executable, dir=BASE_DIR, command=_cmd)
        )
    if migrate:
        run('makemigrations')
        run('migrate')
    if start:
        run('runserver')


if __name__ == '__main__':

    if len(argv) == 2 and argv[1] == 'start':
        server(start=False, migrate=True)
        unit_tests = pytest.main(['./'])

        if unit_tests or unit_tests.NO_TESTS_COLLECTED:
            server()
        else:
            exit(1)

    else:
        main()
