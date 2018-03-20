import pwd
import os
from subprocess import call
from charmhelpers.core.hookenv import startus_set
from charmhelpers.core.templating import render
from charms.reactive import when, when_not, set_state, remove_state


@when('apache.available', 'mysqldatabase.available')
def setup_app(mysql):
    render(source='mysql_configure.php'
        target='/var/www/phpappv1/mysql_configure.php'
        owner='www-data',
        perms=0o775,
        context={
            'db': mysql,
        })
    set_state('apache.start')
    status_set('maintenance', 'Starting apache')


@when('apache.available')
@when_not('mysqldatabase.connected')
def no_mysql_relation():
    remove_state('apache.start')
    status_set('blocked', 'Waiting for mysql relation')


@when('mysqldatabase.connected')
@when_not('mysqldatabase.available')
def mysql_connected_but_waiting(mysql):
    remove_state('apache.start')
    status_set('waiting', 'Waiting for mysql service')

@when('apache.started')
def apache_started():
    status_set('active', 'Ready')