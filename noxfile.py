import nox


@nox.session(tags=["lint"], venv_backend="none")
def fmt_check(s: nox.Session) -> None:
    s.run("isort", "--check", ".")
    s.run("black", "--check", ".")


@nox.session(tags=["formatting"], venv_backend="none")
def fmt(s: nox.Session) -> None:
    s.run("isort", ".")
    s.run("black", ".")


@nox.session(tags=["lint"], venv_backend="none")
def lint(s: nox.Session) -> None:
    s.run("flake8", "--color", "always", "src", "tests")


@nox.session(tags=["lint"], venv_backend="none")
def type_check(s: nox.Session) -> None:
    s.run("mypy", "noxfile.py")
