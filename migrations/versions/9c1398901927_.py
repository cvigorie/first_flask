"""empty message

Revision ID: 9c1398901927
Revises: 
Create Date: 2020-03-07 13:30:30.785220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c1398901927'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('linregresults',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.Column('predicted_salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='ced'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('linregresults', schema='ced')
    # ### end Alembic commands ###
