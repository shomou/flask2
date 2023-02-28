"""modelo usuarios

Revision ID: c7d86551d2aa
Revises: 
Create Date: 2023-02-27 20:47:51.060089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7d86551d2aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('hash_clave', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_usuario_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_usuario_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_usuario_username'))
        batch_op.drop_index(batch_op.f('ix_usuario_email'))

    op.drop_table('usuario')
    # ### end Alembic commands ###
