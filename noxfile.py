import nox

locations = "hypermodern_python_simon994", "tests", "noxfile.py"


@nox.session(python=["3.8", "3.7"])
def tests(session):

    if session.posargs:
        test_files = session.posargs
    else:
        test_files = ["--cov", "-m", "not e2e"]

    session.run("poetry", "install", external=True)
    session.run("pytest", *test_files)


@nox.session(python=["3.8", "3.7"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)
