import nox

@nox.session(python=["3.8", "3.7"])
def tests(session):
        
    if session.posargs:
        test_files = session.posargs
    else:
        test_files = ["--cov"]
    
    session.run("poetry", "install", external=True)
    session.run("pytest", *test_files)