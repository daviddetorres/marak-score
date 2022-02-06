import logging
import argparse
from supply_chain_score.model.context import Context
from supply_chain_score.model.githubrepo import GithubRepo

VERSION = '0.0.1'

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Configure parser
parser = argparse.ArgumentParser(description='Calculate the Supply Chain Score for an open-source repository.')
parser.add_argument('-r',
                    '--repo',
                    required=True,
                    dest='repo',
                    help='The repository to calculate the Supply Chain Score for.')
try:
    args = parser.parse_args()
except BaseException as exception:
    # parser will print either help or syntax error details
    exit(1)

def main():
    """
    Main function.
    """
    # log version
    logger.info('Version: %s', VERSION)

    ctx = Context(logger)


    # Check if the repository is from a valid provider
    # Currently only Github is supported
    if args.repo.startswith('https://github.com/'):
        logger.info('Reading info from the repo {}'.format(args.repo))
        repository = GithubRepo(ctx, args.repo)
    else: 
        logger.error('Repository {} is not from a valid provider'.format(args.repo))
        logger.error('Valid providers: Github')
        exit(1)
        
    print(repository)
if __name__ == '__main__':
    main()