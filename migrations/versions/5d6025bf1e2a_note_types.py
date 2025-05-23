"""note types

Revision ID: 5d6025bf1e2a
Revises: d4201dd0214f
Create Date: 2025-05-22 14:56:36.520894

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d6025bf1e2a'
down_revision: Union[str, None] = 'd4201dd0214f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fragrance_note',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('fragrance_id', sa.BigInteger(), nullable=False),
    sa.Column('note_id', sa.BigInteger(), nullable=False),
    sa.Column('note_type', sa.Enum('TOP', 'MIDDLE', 'BASE', name='notetype'), nullable=False),
    sa.ForeignKeyConstraint(['fragrance_id'], ['fragrance.id'], ),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fragrance_note_fragrance_id'), 'fragrance_note', ['fragrance_id'], unique=False)
    op.create_index(op.f('ix_fragrance_note_note_id'), 'fragrance_note', ['note_id'], unique=False)
    op.drop_table('fragrance_accords_relationship')
    op.create_unique_constraint(None, 'note', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'note', type_='unique')
    op.create_table('fragrance_accords_relationship',
    sa.Column('fragrance_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('note_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['fragrance_id'], ['fragrance.id'], name='fragrance_accords_relationship_fragrance_id_fkey'),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], name='fragrance_accords_relationship_note_id_fkey'),
    sa.PrimaryKeyConstraint('fragrance_id', 'note_id', name='fragrance_accords_relationship_pkey')
    )
    op.drop_index(op.f('ix_fragrance_note_note_id'), table_name='fragrance_note')
    op.drop_index(op.f('ix_fragrance_note_fragrance_id'), table_name='fragrance_note')
    op.drop_table('fragrance_note')
    # ### end Alembic commands ###
