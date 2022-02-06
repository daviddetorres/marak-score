from email import header
import urllib3
from .repo import Repo
import urllib3.request
import json

# child class of Repo for github repos
class GithubRepo(Repo):
    """
    GithubRepo class.
    """

    def __init__(self, ctx, url):
        """
        Initialize GithubRepo class.
        """
        super().__init__(ctx, url)
        
        
    def get_owner(self):
        """
        Return owner of repo.
        """
        return self._parse_github_url(-2, "Getting owner of repo: {}")

    def get_name(self):
        """
        Return name of repo.
        """
        return self._parse_github_url(-1, "Getting name of repo: {}")

    def _parse_github_url(self, position, log_text):
        element_parsed = self.url.split('/')[position]
        self.ctx.logger.info(log_text.format(element_parsed))
        return element_parsed
        
    def _paginated_api_call(self,api_endpoint): 
        """
        Makes a paginated call to get all the results of the call
        Docs on paginated responses here: https://docs.github.com/en/rest/guides/traversing-with-pagination
        """
        http = urllib3.PoolManager()
        headers = {'Accept': 'application/vnd.github.v3+json'}
        try: 
            response = http.request('GET', 
                                    url=api_endpoint+"?per_page=100", 
                                    headers=headers)
        except urllib3.exceptions.MaxRetryError:
            return None
        
        data = json.loads(response.data.decode('utf-8'))
        page_number = 1
        # max number of elements per page is 30. 
        # If there are 30 elements in the response, there are more pages.
        paginate = len(data) == 30
        while paginate:
            page_number += 1
            try: 
                response = http.request('GET', 
                                        url=api_endpoint + "?per_page=100&page={}".format(page_number), 
                                        headers=headers)
            except urllib3.exceptions.MaxRetryError:
                return data
            new_data = json.loads(response.data.decode('utf-8'))
            paginate = len(new_data) == 30
            data.extend(new_data)    
        self.ctx.logger.info("Number of elements retrived: {}".format(len(data)))        
        return data

    def get_contributors(self):  # sourcery skip: class-extract-method
        """
        Return number of contributors for repo using the 
        Github API: https://docs.github.com/en/rest/reference/repos#list-repository-contributors
        GET /repos/{owner}/{repo}/contributors
        """
        self.ctx.logger.info("Getting contributors for repo: {}".format(self.name))
        api_endpoint = "https://api.github.com/repos/{}/{}/contributors".format(self.owner, self.name)
        return (self._paginated_api_call(api_endpoint))

    def get_forks(self):
        """
        Return number of forks for repo using the 
        Github API: https://docs.github.com/en/rest/reference/repos#list-forks
        GET /repos/{owner}/{repo}/forks
        """
        self.ctx.logger.info("Getting forks for repo: {}".format(self.name))
        api_endpoint = "https://api.github.com/repos/{}/{}/forks".format(self.owner, self.name)
        return (self._paginated_api_call(api_endpoint))

    def get_releases(self):
        """
        Return number of releases for repo using the 
        Github API: https://docs.github.com/en/rest/reference/repos#list-releases
        GET /repos/{owner}/{repo}/releases
        """
        self.ctx.logger.info("Getting releases for repo: {}".format(self.name))
        api_endpoint = "https://api.github.com/repos/{}/{}/releases".format(self.owner, self.name)
        return (self._paginated_api_call(api_endpoint))
