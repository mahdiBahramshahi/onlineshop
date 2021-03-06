"""empty message

Revision ID: 5489adf53e35
Revises: 100f6dfd0f81
Create Date: 2021-07-18 20:40:19.102808

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5489adf53e35'
down_revision = '100f6dfd0f81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mahsolgroups', sa.Column('image', sa.String(length=1028), nullable=False))
    op.drop_column('mahsolgroups', 'image_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mahsolgroups', sa.Column('image_link', mysql.VARCHAR(length=128), nullable=False))
    op.drop_column('mahsolgroups', 'image')
    # ### end Alembic commands ###
