from .githubrepo import GithubRepo
from .context import Context
import logging
import pytest
import json
import datetime

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

def test_is_commit_before_date(generate_ctx, generate_commit):
    """
    Test is_commit_before_date function.
    """
    url = "https://github.com/daviddetorres/supply-chain-score"
    repo = GithubRepo(generate_ctx, url)
    commit = generate_commit
    assert repo.is_commit_before_date(commit, datetime.datetime(2070,1,1)) is True
    assert repo.is_commit_before_date(commit, datetime.datetime(1970,1,1)) is False

@pytest.fixture
def generate_ctx():
    """
    Fixture for Context object.
    """
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    return Context(logger)

@pytest.fixture
def generate_commit():
    json_str = """{
        "sha": "0b1337c5d0a4c674287d48622c2a449b5fbe6681",
        "node_id": "C_kwDOGp5OjdoAKDBiMTMzN2M1ZDBhNGM2NzQyODdkNDg2MjJjMmE0NDliNWZiZTY2ODE",
        "commit": {
        "author": {
            "name": "David de Torres",
            "email": "48695803+daviddetorres@users.noreply.github.com",
            "date": "2022-02-07T22:03:17Z"
        },
        "committer": {
            "name": "GitHub",
            "email": "noreply@github.com",
            "date": "2022-02-07T22:03:17Z"
        },
        "message": "Merge pull request #1 from daviddetorres/github-repositories-gather-info\n\nGitHub repositories gather info",
        "tree": {
            "sha": "741ed1d6848f2a6bea05a53bc05775893fc014cc",
            "url": "https://api.github.com/repos/daviddetorres/supply-chain-score/git/trees/741ed1d6848f2a6bea05a53bc05775893fc014cc"
        },
        "url": "https://api.github.com/repos/daviddetorres/supply-chain-score/git/commits/0b1337c5d0a4c674287d48622c2a449b5fbe6681",
        "comment_count": 0,
        "verification": {
            "verified": true,
            "reason": "valid",
            "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJiAZclCRBK7hj4Ov3rIwAAHlcIAHpJ2MB5PTN0fSscZwAGjEOW\ngLq49rQnbQRJtQUq4/hTJIVCdT5qLCIMBB1hi3DIBUjGEiefpaZmqKTM69GIC4XK\ndqxOtjpyAU2jfBVlNR2rx64i+wR6EYc18ckt/LHkHM6HO2MTVUbKPTQ/n9JqFS3B\n4ilgHug9YrjsdAxLC1rI5/P8G6u6Z2u+ZHv2clCV1P4WR4Jv2wzC8NdvJoLPbLdK\nX39r3Qc4W8YwusOzgf5x19IV9iWiyHHKInYX/hd3iB/LGYWH59cA6Ys1JSOde6/z\nGn8u8HAPUAaC/Dr+9/p/a4dVyRi2RDFzcExypIKw0yJmKlEr4uOYKScF5NIqQTE=\n=o5Ug\n-----END PGP SIGNATURE-----\n",
            "payload": "tree 741ed1d6848f2a6bea05a53bc05775893fc014cc\nparent d6d726bb363ecc337f2c71deff4076d98dfff653\nparent 5a87a441d7f0efdf165543f8c2626d1aa2bf727c\nauthor David de Torres <48695803+daviddetorres@users.noreply.github.com> 1644271397 +0100\ncommitter GitHub <noreply@github.com> 1644271397 +0100\n\nMerge pull request #1 from daviddetorres/github-repositories-gather-info\n\nGitHub repositories gather info"
        }
        },
        "url": "https://api.github.com/repos/daviddetorres/supply-chain-score/commits/0b1337c5d0a4c674287d48622c2a449b5fbe6681",
        "html_url": "https://github.com/daviddetorres/supply-chain-score/commit/0b1337c5d0a4c674287d48622c2a449b5fbe6681",
        "comments_url": "https://api.github.com/repos/daviddetorres/supply-chain-score/commits/0b1337c5d0a4c674287d48622c2a449b5fbe6681/comments",
        "author": {
        "login": "daviddetorres",
        "id": 48695803,
        "node_id": "MDQ6VXNlcjQ4Njk1ODAz",
        "avatar_url": "https://avatars.githubusercontent.com/u/48695803?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/daviddetorres",
        "html_url": "https://github.com/daviddetorres",
        "followers_url": "https://api.github.com/users/daviddetorres/followers",
        "following_url": "https://api.github.com/users/daviddetorres/following{/other_user}",
        "gists_url": "https://api.github.com/users/daviddetorres/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/daviddetorres/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/daviddetorres/subscriptions",
        "organizations_url": "https://api.github.com/users/daviddetorres/orgs",
        "repos_url": "https://api.github.com/users/daviddetorres/repos",
        "events_url": "https://api.github.com/users/daviddetorres/events{/privacy}",
        "received_events_url": "https://api.github.com/users/daviddetorres/received_events",
        "type": "User",
        "site_admin": false
        },
        "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "site_admin": false
        },
        "parents": [
        {
            "sha": "d6d726bb363ecc337f2c71deff4076d98dfff653",
            "url": "https://api.github.com/repos/daviddetorres/supply-chain-score/commits/d6d726bb363ecc337f2c71deff4076d98dfff653",
            "html_url": "https://github.com/daviddetorres/supply-chain-score/commit/d6d726bb363ecc337f2c71deff4076d98dfff653"
        },
        {
            "sha": "5a87a441d7f0efdf165543f8c2626d1aa2bf727c",
            "url": "https://api.github.com/repos/daviddetorres/supply-chain-score/commits/5a87a441d7f0efdf165543f8c2626d1aa2bf727c",
            "html_url": "https://github.com/daviddetorres/supply-chain-score/commit/5a87a441d7f0efdf165543f8c2626d1aa2bf727c"
        }
        ]
    }"""
    return json.loads(json_str, strict=False)