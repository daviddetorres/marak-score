# The Supply Chain Score
The **Supply Chain Score** is a simple score system to evaluate the risk of an open source repository.

Repositories with high score tend to be highly used and well maintained. Well maintained repositories tend to have a high number of different contributors, high frequency of commits, and high number of issues.

Repositories with high score have different risks. Some of the risks are:
* Security issues. The best example of this is log4j, a repository highly used and maintained by a bunch of developers as a side project that provoked a [high security issue in December 2021](https://logging.apache.org/log4j/2.x/security.html).
* Maintainers hijacking the repository. There are many examples of maintainers removing or modifying the code of a repository in malicious ways. One of them was [Marak](https://github.com/Marak), who removed the code of the `faker.js` and `colors.js` repositories.

## How does the Supply Chain Score works?
The Supply Chain Score gives a rating to a repository based on its past and recent activity. 

Things like the number of different commiters, frequency of the commits, forks, oranizations behind the project... All these things give points to the rpeository to finally get a calification, from A (best) to F (worst).
