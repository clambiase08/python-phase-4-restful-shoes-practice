"""Initial migration.

Revision ID: 4e798a125f43
Revises: 
Create Date: 2023-08-16 14:28:18.407680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e798a125f43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('style', sa.String(), nullable=True),
    sa.Column('size', sa.Float(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.Column('inventory', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects')
    # ### end Alembic commands ###