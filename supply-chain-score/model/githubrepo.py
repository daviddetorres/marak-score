import urllib3
from repo import Repo
import urllib3.request
import json

# child class of Repo for github repos
class GithubRepo(Repo):
    """
    GithubRepo class.
    """

    def __init__(self, url):
        """
        Initialize GithubRepo class.
        """
        super().__init__(url)
        
        
    def get_owner(self):
        """
        Return owner of repo.
        """
        return self.url.split("/")[-2]

    def get_name(self):
        """
        Return name of repo.
        """
        return self.url.split("/")[-1]
        
    def paginated_api_call(self,api_endpoint): 
        """
        Makes a paginated call to get all the results of the call
        Docs on paginated responses here: https://docs.github.com/en/rest/guides/traversing-with-pagination
        """
        request = urllib3.request.Request(api_endpoint)
        request.add_header("Accept", "application/vnd.github.v3+json")
        response = urllib3.request.urlopen(request)
        response_data = json.loads(response.read())
        page_number = 1
        # max number of elements per page is 30. 
        # If there are 30 elements in the response, there are more pages.
        while len(response_data) == 30:
            page_number += 1
            request = urllib3.request.Request(api_endpoint + "?page={}".format(page_number))
            request.add_header("Accept", "application/vnd.github.v3+json")
            response = urllib3.request.urlopen(request)
            response_data += json.loads(response.read())
        return response_data

    def get_contributors(self):
        """
        Return number of contributors for repo using the 
        Github API: https://docs.github.com/en/rest/reference/repos#list-repository-contributors
        GET /repos/{owner}/{repo}/contributors
        """
        api_endpoint = "https://api.github.com/repos/{}/{}/contributors".format(self.owner, self.name)
        return (self.paginated_api_call(api_endpoint))

    def get_forks(self):
        """
        Return number of forks for repo using the 
        Github API: https://docs.github.com/en/rest/reference/repos#list-forks
        GET /repos/{owner}/{repo}/forks
        """
        api_endpoint = "https://api.github.com/repos/{}/{}/forks".format(self.owner, self.name)
        return (self.paginated_api_call(api_endpoint))

    def get_releases(self):
        """
        Return number of releases for repo using the 
        Github API: https://docs.github.com/en/rest/reference/repos#list-releases
        GET /repos/{owner}/{repo}/releases
        """
        api_endpoint = "https://api.github.com/repos/{}/{}/releases".format(self.owner, self.name)
        return (self.paginated_api_call(api_endpoint))
