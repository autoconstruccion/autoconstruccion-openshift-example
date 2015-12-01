import os

# propagate exceptions so OpenShift Logs be aware of.
PROPAGATE_EXCEPTIONS=True

SQLALCHEMY_DATABASE_URI="postgresql://{}:{}@{}:{}/autoconstruccion".format(os.getenv('OPENSHIFT_POSTGRESQL_DB_USERNAME'), os.getenv('OPENSHIFT_POSTGRESQL_DB_PASSWORD'), os.getenv('OPENSHIFT_POSTGRESQL_DB_HOST'), os.getenv('OPENSHIFT_POSTGRESQL_DB_PORT') )

