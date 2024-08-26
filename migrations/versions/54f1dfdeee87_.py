"""empty message

<<<<<<<< HEAD:migrations/versions/43dae602d453_.py
Revision ID: 43dae602d453
Revises: 
Create Date: 2024-08-21 14:07:34.672954
========
Revision ID: 54f1dfdeee87
Revises: 
Create Date: 2024-08-21 15:25:56.459178
>>>>>>>> bf5787c33f7c0483124a48ccde7b2aa6944dff87:migrations/versions/54f1dfdeee87_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:migrations/versions/43dae602d453_.py
revision = '43dae602d453'
========
revision = '54f1dfdeee87'
>>>>>>>> bf5787c33f7c0483124a48ccde7b2aa6944dff87:migrations/versions/54f1dfdeee87_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercise',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('category', sa.Enum('PECHO', 'ESPALDA', 'PIERNA', 'HOMBRO', 'TRAPECIO', 'ABDOMEN', name='category'), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('sets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sets', sa.Integer(), nullable=False),
    sa.Column('repetitions', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('sex', sa.Enum('male', 'female', name='sex'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('physical_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('routine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('exercise_routine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('routine_id', sa.Integer(), nullable=False),
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.Column('sets_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercise.id'], ),
    sa.ForeignKeyConstraint(['routine_id'], ['routine.id'], ),
    sa.ForeignKeyConstraint(['sets_id'], ['sets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weekly_routine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('routine_id', sa.Integer(), nullable=False),
    sa.Column('day', sa.Enum('LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES', 'SABADO', 'DOMINGO', name='day'), nullable=False),
    sa.ForeignKeyConstraint(['routine_id'], ['routine.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('follow_up',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weekly_routine_id', sa.Integer(), nullable=False),
    sa.Column('exercise_routine_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['exercise_routine_id'], ['exercise_routine.id'], ),
    sa.ForeignKeyConstraint(['weekly_routine_id'], ['weekly_routine.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follow_up')
    op.drop_table('weekly_routine')
    op.drop_table('exercise_routine')
    op.drop_table('routine')
    op.drop_table('physical_information')
    op.drop_table('user')
    op.drop_table('sets')
    op.drop_table('exercise')
    # ### end Alembic commands ###
