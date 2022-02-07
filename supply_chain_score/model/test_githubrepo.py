from .githubrepo import GithubRepo
from .context import Context
import logging
import pytest

@pytest.fixture
def generate_ctx():
    """
    Fixture for Context object.
    """
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    return Context(logger)

def test_init_with_url(generate_ctx):
    """
    Test init function.
    """
    url = "https://github.com/daviddetorres/supply-chain-score"
    repo = GithubRepo(generate_ctx, url)
    assert repo.url == url
    assert repo.owner == "daviddetorres"
    assert repo.name == "supply-chain-score"

def test_get_api_url_with_extra_params():
    """
    Test get_api_url function.
    """
    api_endpoint = "https://api.github.com/repos/a/a/issues"
    url = GithubRepo.get_api_url(api_endpoint, "state=all")
    assert url == "https://api.github.com/repos/a/a/issues?state=all&per_page={}".format(GithubRepo.max_elements_per_page)

def test_get_api_url_without_extra_params():
    """
    Test get_api_url function.
    """
    api_endpoint = "https://api.github.com/repos/a/a/issues"
    # Optional parameter must be provided as None as the class is not instantiated.
    url = GithubRepo.get_api_url(api_endpoint, None)
    assert url == "https://api.github.com/repos/a/a/issues?per_page={}".format(GithubRepo.max_elements_per_page)
