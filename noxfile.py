import nox


@nox.session(python=["3.11"], reuse_venv=False)
def tests(session):
    session.install("poetry")
    session.run("poetry", "install", "--with", "dev", external=True)
    session.run("pytest", "tests/", "--cov=src/")
