"""empty message

Revision ID: 9c780a50264e
Revises: 
Create Date: 2024-07-09 15:26:41.359496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c780a50264e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lit_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('surname', sa.String(length=64), nullable=True),
    sa.Column('date', sa.String(length=64), nullable=True),
    sa.Column('time', sa.String(length=64), nullable=True),
    sa.Column('part', sa.String(length=64), nullable=True),
    sa.Column('defects', sa.String(length=64), nullable=True),
    sa.Column('reason', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('lit_results', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_lit_results_date'), ['date'], unique=False)
        batch_op.create_index(batch_op.f('ix_lit_results_defects'), ['defects'], unique=False)
        batch_op.create_index(batch_op.f('ix_lit_results_part'), ['part'], unique=False)
        batch_op.create_index(batch_op.f('ix_lit_results_reason'), ['reason'], unique=False)
        batch_op.create_index(batch_op.f('ix_lit_results_surname'), ['surname'], unique=False)
        batch_op.create_index(batch_op.f('ix_lit_results_time'), ['time'], unique=False)

    op.create_table('parts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('part', sa.String(length=64), nullable=True),
    sa.Column('part_type', sa.String(length=64), nullable=True),
    sa.Column('part_group', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('parts', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_parts_part'), ['part'], unique=False)
        batch_op.create_index(batch_op.f('ix_parts_part_group'), ['part_group'], unique=False)
        batch_op.create_index(batch_op.f('ix_parts_part_type'), ['part_type'], unique=False)

    op.create_table('seal_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('surname', sa.String(length=64), nullable=True),
    sa.Column('date', sa.String(length=64), nullable=True),
    sa.Column('time', sa.String(length=64), nullable=True),
    sa.Column('part', sa.String(length=64), nullable=True),
    sa.Column('defects', sa.String(length=64), nullable=True),
    sa.Column('reason', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('seal_results', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_seal_results_date'), ['date'], unique=False)
        batch_op.create_index(batch_op.f('ix_seal_results_defects'), ['defects'], unique=False)
        batch_op.create_index(batch_op.f('ix_seal_results_part'), ['part'], unique=False)
        batch_op.create_index(batch_op.f('ix_seal_results_reason'), ['reason'], unique=False)
        batch_op.create_index(batch_op.f('ix_seal_results_surname'), ['surname'], unique=False)
        batch_op.create_index(batch_op.f('ix_seal_results_time'), ['time'], unique=False)

    op.create_table('thread_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('surname', sa.String(length=64), nullable=True),
    sa.Column('date', sa.String(length=64), nullable=True),
    sa.Column('time', sa.String(length=64), nullable=True),
    sa.Column('part', sa.String(length=64), nullable=True),
    sa.Column('defects', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('thread_results', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_thread_results_date'), ['date'], unique=False)
        batch_op.create_index(batch_op.f('ix_thread_results_defects'), ['defects'], unique=False)
        batch_op.create_index(batch_op.f('ix_thread_results_part'), ['part'], unique=False)
        batch_op.create_index(batch_op.f('ix_thread_results_surname'), ['surname'], unique=False)
        batch_op.create_index(batch_op.f('ix_thread_results_time'), ['time'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('fio', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_fio'), ['fio'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_fio'))

    op.drop_table('user')
    with op.batch_alter_table('thread_results', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_thread_results_time'))
        batch_op.drop_index(batch_op.f('ix_thread_results_surname'))
        batch_op.drop_index(batch_op.f('ix_thread_results_part'))
        batch_op.drop_index(batch_op.f('ix_thread_results_defects'))
        batch_op.drop_index(batch_op.f('ix_thread_results_date'))

    op.drop_table('thread_results')
    with op.batch_alter_table('seal_results', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_seal_results_time'))
        batch_op.drop_index(batch_op.f('ix_seal_results_surname'))
        batch_op.drop_index(batch_op.f('ix_seal_results_reason'))
        batch_op.drop_index(batch_op.f('ix_seal_results_part'))
        batch_op.drop_index(batch_op.f('ix_seal_results_defects'))
        batch_op.drop_index(batch_op.f('ix_seal_results_date'))

    op.drop_table('seal_results')
    with op.batch_alter_table('parts', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_parts_part_type'))
        batch_op.drop_index(batch_op.f('ix_parts_part_group'))
        batch_op.drop_index(batch_op.f('ix_parts_part'))

    op.drop_table('parts')
    with op.batch_alter_table('lit_results', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_lit_results_time'))
        batch_op.drop_index(batch_op.f('ix_lit_results_surname'))
        batch_op.drop_index(batch_op.f('ix_lit_results_reason'))
        batch_op.drop_index(batch_op.f('ix_lit_results_part'))
        batch_op.drop_index(batch_op.f('ix_lit_results_defects'))
        batch_op.drop_index(batch_op.f('ix_lit_results_date'))

    op.drop_table('lit_results')
    # ### end Alembic commands ###
