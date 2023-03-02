"""modelo usuarios

Revision ID: af6372069796
Revises: 08914e46310c
Create Date: 2023-03-01 20:46:51.198886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af6372069796'
down_revision = '08914e46310c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sobre_mi', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('ultima_sesion', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_usuario_ultima_sesion'), ['ultima_sesion'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_usuario_ultima_sesion'))
        batch_op.drop_column('ultima_sesion')
        batch_op.drop_column('sobre_mi')

    # ### end Alembic commands ###
