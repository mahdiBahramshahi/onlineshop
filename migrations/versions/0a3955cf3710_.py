"""empty message

Revision ID: 0a3955cf3710
Revises: de3a86bb68e1
Create Date: 2021-06-01 09:35:57.272682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a3955cf3710'
down_revision = 'de3a86bb68e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(length=128), nullable=False))
    op.drop_index('email', table_name='users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('email', 'users', ['email'], unique=False)
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
