from ckan.lib.cli import CkanCommand

from logging import getLogger
import sys
import click

log = getLogger(__name__)


def get_commands():
    return [issues]


@click.group(short_help=u"Issues extension commands")
def issues():
    pass


@issues.command(short_help=u"Creates the database table issues needs to run")
def init_db():
    from ckanext.issues.model import setup
    setup()
    log.info('Issues tables are initialized.')


@issues.command(short_help=u"Does any database migrations required (idempotent)")
def upgrade_db():
    from ckanext.issues.model import upgrade
    upgrade()
    log.info('Issues tables are up to date.')
