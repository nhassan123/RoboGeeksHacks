"""pump table

Revision ID: ede6e1562f96
Revises: c5b363ae05c7
Create Date: 2018-08-27 15:36:49.647924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ede6e1562f96'
down_revision = 'c5b363ae05c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entry', sa.Column('profile', sa.String(length=25), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('entry', 'profile')
    # ### end Alembic commands ###
