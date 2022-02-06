from .githubrepo import GithubRepo

def test_get_api_url_with_extra_params():
    """
    Test get_api_url function.
    """
    api_endpoint = "https://api.github.com/repos/a/a/issues"
    url = GithubRepo.get_api_url(api_endpoint, "state=all")
    assert url == "https://api.github.com/repos/a/a/issues?state=all&per_page=100"

def test_get_api_url_without_extra_params():
    """
    Test get_api_url function.
    """
    api_endpoint = "https://api.github.com/repos/a/a/issues"
    # Optional parameter must be provided as None as the class is not instantiated.
    url = GithubRepo.get_api_url(api_endpoint, None)
    assert url == "https://api.github.com/repos/a/a/issues?per_page=100"
