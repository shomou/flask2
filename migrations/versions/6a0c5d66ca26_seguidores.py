"""seguidores


Revision ID: 6a0c5d66ca26
Revises: 7f56a09da4f0
Create Date: 2023-03-02 00:19:42.616133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a0c5d66ca26'
down_revision = '7f56a09da4f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seguidores',
    sa.Column('seguidor_id', sa.Integer(), nullable=True),
    sa.Column('seguido_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seguido_id'], ['usuario.id'], ),
    sa.ForeignKeyConstraint(['seguidor_id'], ['usuario.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seguidores')
    # ### end Alembic commands ###
