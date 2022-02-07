

class Repo:
    """
    Repo class.
    """

    def __init__(self, ctx, url):
        """
        Initialize Repo class.
        """
        self.ctx = ctx
        self.url = url
        self.owner = self.get_owner()
        self.name = self.get_name()


    def __str__(self):
        """
        Return string representation of Repo object.
        """
        info = "Repo: {0}\n".format(self.url)
        info += "  Owner: {0}\n".format(self.owner)
        info += "  Name: {0}\n".format(self.name)
        info += "  Number of Contributors: {0}\n".format(self.total_contributors)
        info += "  Number of Forks: {0}\n".format(self.total_forks)
        info += "  Number of Releases: {0}\n".format(self.total_releases)
        info += "  Number of Issues: {0}\n".format(self.total_issues)
        return info

    def get_data(self):
        """
        Return data for repo.
        """
        self.contributors = self.get_contributors()
        self.forks = self.get_forks()
        self.releases = self.get_releases()
        self.issues = self.get_issues()
        self.commits = self.get_commits()        
        self.stars = self.get_stars()

    def calculate_statistics(self):
        """
        Calculate statistics for repo.
        """
        self.total_contributors = self.get_total_contributors()
        self.total_forks = self.get_total_forks()
        self.total_releases = self.get_total_releases()
        self.total_issues = self.get_total_issues()
    

    def get_contributors(self):
        """
        Return number of contributors for repo.
        """
        pass

    def get_forks(self):
        """
        Return number of forks for repo.
        """
        pass

    def get_releases(self):
        """
        Return number of releases for repo.
        """
        pass

    def get_stars(self):
        """
        Return number of stars for repo.
        """
        pass
    

    def get_issues(self):
        """
        Return number of issues for repo.
        """
        pass


    def get_commits(self):
        """
        Return number of commits for repo.
        """
        pass
    
    def get_total_contributors(self):
        """
        Return total number of contributors for repo.
        """
        pass

    def get_total_forks(self):
        """
        Return total number of forks for repo.
        """
        pass

    def get_total_releases(self):
        """
        Return total number of releases for repo.
        """
        pass

    def get_total_issues(self):
        """
        Return total number of issues for repo.
        """
        pass

    def get_score(self):
        """
        Return score for repo.
        """
        pass
