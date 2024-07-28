import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--platform", action="store", default="ios", help="platform: ios or android"
    )

@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform")
