"""empty message

Revision ID: ed5db9624b3c
Revises: 
Create Date: 2020-08-19 21:13:25.789251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed5db9624b3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('strain',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('strain', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('effects', sa.String(), nullable=True),
    sa.Column('flavor', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('strain')
    # ### end Alembic commands ###